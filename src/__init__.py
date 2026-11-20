from typing import Callable , Any
from functools import wraps
from src.app import App

class Decorix(App):
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