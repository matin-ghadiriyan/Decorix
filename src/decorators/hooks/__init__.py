from functools import wraps
from typing import Callable , Any
from src.decorators.hooks.BaseHooks import BaseHooks

class Before(BaseHooks):
    TYPE = "Before"
    def __init__(self):
        super().__init__()

    def before(
        self,
        key:str
    ) -> Any:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs)->Any:
                self.get_data(self._dictionary, key)()
                return func(*args, **kwargs)
            return wrapper
        return decorator

class After(BaseHooks):
    TYPE = "After"
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
                self.get_data(
                    self._dictionary,
                    key
                )(resulte)
                return resulte
            return wrapper
        return decorator

class Finally(BaseHooks):
    TYPE = "Finally"
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
                    result = func(*args, **kwargs)
                    return result
                finally:
                    self.get_data(self._dictionary, key)()
            return wrapper
        return decorator