from src.decorators.User.register_login_user import _Register_Login_User
from src.models import Model_User
from typing import Any
from src.exceptions import TypeIsNotValid

class User(Model_User , _Register_Login_User):
    def __init__(self , username:str , password:str) -> None:super().__init__(username , password)
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