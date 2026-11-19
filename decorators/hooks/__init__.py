from functools import wraps
from typing import Callable , Any
from decorators.hooks.BaseHooks import BaseHooks
from BaseClass import BaseClass

class Before(BaseHooks , BaseClass):
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
                super().get_data(self._dictionary, key)()
                return func(*args, **kwargs)
            return wrapper
        return decorator

class After(BaseHooks , BaseClass):
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
                super().get_data(
                    self._dictionary,
                    key
                )(resulte)
                return resulte
            return wrapper
        return decorator

class Finally(BaseHooks , BaseClass):
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
                    resulte = func(*args, **kwargs)
                finally:
                    resulte = super().get_data(
                        self._dictionary,
                        key
                    )()
                return resulte
            return wrapper
        return decorator