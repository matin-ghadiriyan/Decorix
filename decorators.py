from functools import wraps
from typing import Callable, Any

class Decorator:
    #--- setting class ---
    def __init__(self):
        self._afters: dict = {}
        self._befores: dict = {}
        self._finallys: dict = {}

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
        self._afters:dict = value

    @property
    def finallys(self):
        if not isinstance(self._finallys, dict):
            raise TypeError(f"Expected dict, got {type(self._finallys).__name__}")
        return self._finallys
    
    @finallys.setter
    def finallys(self, value):
        if not isinstance(value, dict):
            raise TypeError(f"Expected dict, got {type(value).__name__}")
        self._finallys:dict = value

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
        *funcs: Callable
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

    def add_finally(self, **func: dict[str, Callable]) -> None:
        "add function to finally"
        self._check_str_callable(**func)
        self.finallys.update(func)

    def before(self, key: str) -> Callable:
        "get function from before"
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                if key in self.befores:
                    self.befores[key](*args,**kwargs)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def after(self, key: str) -> Callable:
        "get function from after"
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                result = func(*args, **kwargs)
                if key in self.afters:
                    self.afters[key](result,*args,**kwargs)
                return result
            return wrapper
        return decorator

    def finall(
        self, key: str
    ) -> Callable:
        "get function from finally"
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                result = None
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    if key in self.finallys:
                        self.finallys[key](result, *args, **kwargs)
            return wrapper
        return decorator

    def remove_after(
        self,
        key: str
    ) -> None:
        "remove function from after"
        if key in self.afters:
            del self.afters[key]
    def remove_before(
        self,
        key: str
    ) -> None:
        "remove function from before"
        if key in self.befores:
            del self.befores[key]

    def remove_finally(
        self,
        key:str
    ) -> None:
        if key in self.finallys:
            del self.finallys[key]
    