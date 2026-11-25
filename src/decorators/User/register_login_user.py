from typing import Any, Callable, Dict , Type , TypeVar , List
from functools import wraps
from werkzeug.security import check_password_hash , generate_password_hash
from src.models import Model_User
from src.exceptions import ValueIsNotValid , PasswordIsNotValid

T = TypeVar("T" , bound=Model_User)

class _Register_Login_User_Password():
    def hash(self, password:str) -> str:return generate_password_hash(password)
    def check_hash(self, password:str, hash:str) -> bool: return check_password_hash(hash, password)

class _Register_Login_User(_Register_Login_User_Password):
    def __init__(self) -> None:
        self.logins:Dict[str, Dict[str, bool | Type[T]]] = {}
        self.logsout:Dict[str, Callable | List | Dict[str, Any] | None] = {
            "func": None,
            "args": None,
            "kwargs": None
        }

    def register(
        self,
        func:Callable
    ) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            model:Type[T] = func(*args, **kwargs)
            model.password = self.hash(model.password)
            self.logins[model.username] = {
                "model": model,
                "login":True
            }
            
        return wrapper

    def _current_model(self, username:str) -> Type[T]:return self.logins.get(username).get("model")

    def login(self, username:str, password:str) -> Type[T]:
        model:Type[T] = self._current_model(username)
        if model is None:raise ValueIsNotValid('User not found')
        elif not self.check_hash(model.password, password):raise PasswordIsNotValid('Password is not valid')
        elif not self.logins.get(username).get("login"):raise ValueIsNotValid('User already logout')
        return model

    def change_password(
        self,
        username:str,
        old_password:str,
        new_password:str
    ) -> None:
        model = self._current_model(username)
        if model is None:raise ValueIsNotValid('User not found')
        if self.check_hash(
            password=old_password,
            hash=model.password
        ):model.password = self.hash(new_password)
        raise PasswordIsNotValid('Password is not valid')

    def register_logout(self, func:Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.logsout['func'] = func
            self.logsout['args'] = args
            self.logsout['kwargs'] = kwargs

        return wrapper

    def logout(
        self,
        username:str
    ):
        model = self._current_model(username)
        if model is None:raise ValueIsNotValid('User not found')
        elif self.logins.get(username).get('login'):
            self.logins[username]['login'] = False
            self.logsout['func'](*self.logsout['args'], **self.logsout['kwargs'])
        

    