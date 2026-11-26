from src.decorators.hooks import After , Before , Finally , Handler
from src.models import Model_User as U
from src.decorators.User import User

class App():
    def __init__(self):
        self._Befores = Before()
        self._Afters = After()
        self._Finallys = Finally()
        self._Handlers = Handler()
        self._User = User()

    def b(self) -> Before:return self._Befores
    def a(self) -> After:return self._Afters
    def f(self) -> Finally:return self._Finallys
    def h(self) -> Handler:return self._Handlers

    class Model(U):...
    def user(self) -> User:return self._User