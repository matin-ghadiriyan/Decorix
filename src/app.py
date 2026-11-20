from src.decorators.hooks import After , Before , Finally , Handler

class App():
    def __init__(self):
        self._Befores = Before()
        self._Afters = After()
        self._Finallys = Finally()
        self._Handlers = Handler()

    def b(self) -> Before:return self._Befores
    def a(self) -> After:return self._Afters
    def f(self) -> Finally:return self._Finallys
    def h(self) -> Handler:return self._Handlers
    