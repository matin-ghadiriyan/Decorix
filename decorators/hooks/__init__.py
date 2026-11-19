from functools import wraps
from typing import Callable , Any
from decorators.hooks.BaseHooks import BaseHooks

class Before(BaseHooks):
    TYPE:str = "Before"
    def __init__(self):
        super().__init__()

    def before(
        self,
        key:str
    ) -> Any:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs)->Any:
                if self._dictionary[key]:
                    self._dictionary[key]()
                return func(*args, **kwargs)
            return wrapper
        return decorator

class After(BaseHooks):
    TYPE:str = "After"
    def __init__(self):
        super().__init__()

    def after(
        self,
        key:str
    ) -> Any:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                resulte = func(*args, **kwargs)
                if self._dictionary[key]:
                    self._dictionary.get(key)()
                return resulte
            return wrapper
        return decorator

class Finally(BaseHooks):
    TYPE:str = "Finally"
    def __init__(self):
        super().__init__()

    def _finally(
        self,
        key:str
    ) -> Any:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    func(*args, **kwargs)
                finally:
                    if self._dictionary[key]:
                        self._dictionary.get(key)()
            return wrapper
        return decorator