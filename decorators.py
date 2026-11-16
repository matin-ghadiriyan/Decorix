from functools import wraps

class Decorator:
    def __str__(self):
        return "Decorator()"

    def decorate(
        self,
        error: callable,
        *funcs:list[callable]
    )-> callable:
        """Decorator for functions"""
        def decorator(func:callable)-> callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                for f in funcs:
                    if not f:
                        error
                return func(*args, **kwargs)
            return wrapper
        return decorator