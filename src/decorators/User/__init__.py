from src.decorators.User.register_login_user import _Register_Login_User
from typing import Any , Callable
from src.exceptions import TypeIsNotValid , UserIsNotLoggedIn
from functools import wraps

class User(_Register_Login_User):
    def __init__(self) -> None:
        super().__init__()
    def _check_type(self, value:Any, types:Any) -> Any:
        if not isinstance(value , types):raise TypeIsNotValid(f"Value {value} is not {types}")
        else:return value
    @property
    def username_check(self) -> str:return self._check_type(self.username , str)
    @property
    def password_check(self) -> str:return self._check_type(self.password , str)
    @username_check.setter
    def username_check(self, value:Any) -> None:self.username = self._check_type(value , str)
    @password_check.setter
    def password_check(self, value:Any) -> None:self.password = self._check_type(value , str)
    
    def is_logging(self, username:str) -> Callable:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                if self.logins.get(username).get("login"):
                    return func(*args, **kwargs)
                else:raise UserIsNotLoggedIn("User is not logged in")
            
            return wrapper
        return decorator