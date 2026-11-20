from typing import Any , Callable , List , Dict , TYPE_CHECKING
from src.exceptions import ValueIsNotValid , TypeIsNotValid , KeyIsAlreadyExists
from src.BaseClass import BaseClass

if TYPE_CHECKING:
    from .BaseHooks import BaseHooks

class ReadDeleteHooks():
    "Read Data"
    def get_key(self:"BaseHooks") -> List[str]:return list(self._keys)
    def get_funcs(self:"BaseHooks") -> List[Callable]:return list(self._funcs)
    def get_dictionary(self:"BaseHooks") -> Dict[str : Callable]:return dict(self._dictionary)
    "Remove Data"
    def removes_all(self:"BaseHooks") -> None:
        self._funcs.clear()
        self._keys.clear()
        self._dictionary.clear()

class BaseHooks(ReadDeleteHooks, BaseClass):
    TYPE = None
    def __init__(self):
        self._funcs: List[Callable] = []
        self._keys: List[str] = []
        self._dictionary: Dict[str, Callable] = {}

    def register(
        self,
        **funcs: Callable
    ) -> None:
        for key, func in funcs.items():
            if not super().check_type(
                valid_type=Callable,
                value=func
            ):
                raise TypeIsNotValid(
                    f"{type(func).__name__} is not valid"
                )
            elif not super().check_type(
                valid_type=str,
                value=key
            ):
                raise TypeIsNotValid(
                    f"{type(key).__name__} is not valid"
                )
            elif key in self._dictionary:
                raise KeyIsAlreadyExists(
                    f"{key} is already exists"
                )
            else:
                self._funcs.append(func)
                self._keys.append(key)
                self._dictionary[key] = func

    @property
    def func(self) -> List[Callable]:
        if isinstance(self._funcs, list):
            for funcs in self._funcs:
                if not callable(funcs):
                    raise ValueIsNotValid(f"{type(funcs).__name__} is not a valid function")
            return self._funcs.copy()
        raise ValueIsNotValid(f"{type(self._funcs).__name__} is not a valid list")

    @property
    def key(self) -> List[str]:
        if isinstance(self._keys, list):
            for key in self._keys:
                if not isinstance(key, str):
                    raise ValueIsNotValid(f"{type(key).__name__} is not a valid string")
            return self._keys.copy()
        raise ValueIsNotValid(f"{type(self._keys).__name__} is not a valid list")  

    @property
    def dictionarys(self) -> Dict[str, Any]:
        if isinstance(self._dictionary, dict):
            for key, value in self._dictionary.items():
                if not isinstance(key, str):
                    raise ValueIsNotValid(f"{type(key).__name__} is not a valid string")
                elif not callable(value):
                    raise ValueIsNotValid(f"{type(value).__name__} is not a valid function")
            return self._dictionary.copy()
        raise ValueIsNotValid(f"{type(self._dictionary).__name__} is not a valid dictionary")
