from functools import wraps
from typing import Callable, Any

class Decorator:
    #--- setting class ---
    def __init__(self):
        self._afters: dict = {}
        self._befores: dict = {}

    def __str__(self) -> str:
        return "Decorator()"

    # --- getter and setter ---
    @property
    def afters(self):
        if not isinstance(self._afters, dict):
            raise TypeError(f"Expected dict, got {type(self._afters).__name__}")
        return self._afters

    @afters.setter
    def afters(self, value):
        if not isinstance(value, dict):
            raise TypeError(f"Expected dict, got {type(value).__name__}")
        self._afters = value

    @property
    def befores(self):
        if not isinstance(self._befores, dict):
            raise TypeError(f"Expected dict, got {type(self._befores).__name__}")
        return self._befores
    
    @befores.setter
    def befores(self, value):
        if not isinstance(value, dict):
            raise TypeError(f"Expected dict, got {type(value).__name__}")
        self._befores = value  

    # --- functions ---
    def validate(
        self,
        error: Callable,
        *funcs: list[Callable]
    ) -> Callable:
        """Decorator for functions"""

        def decorator(func: Callable) -> Callable:

            @wraps(func)
            def wrapper(*args: tuple, **kwargs: dict) -> Any:
                for f in funcs:
                    if not f():
                        return error()
                return func(*args, **kwargs)

            return wrapper
        
        return decorator

    def _check_str_callable(self, **func: dict[str, Callable]) -> None:
        "check type of func"
        for k, v in func.items():
            if not isinstance(k, str):
                raise TypeError(f"Key must be a string, not {type(k).__name__}")
            if not callable(v):
                raise TypeError(f"Value must be a callable, not {type(v).__name__}")
        
    def add_after(self, **func: dict[str, Callable]) -> None:
        "add function to after"
        self._check_str_callable(**func)
        self.afters.update(func)

    def add_before(self, **func: dict[str, Callable]) -> None:
        "add function to before"
        self._check_str_callable(**func)
        self.befores.update(func)

    def before(self, key: str) -> Callable:
        "get function from before"
        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs) -> Any:
                if key in self.befores:
                    self.befores[key](*args,%20**kwargs)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def after(self, key: str) -> Callable:
        "get function from after"
        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs) -> Any:
                result = func(*args, **kwargs)
                if key in self.afters:
                    self.afters[key](result,%20*args,%20**kwargs)
                return result
            return wrapper
        return decorator
