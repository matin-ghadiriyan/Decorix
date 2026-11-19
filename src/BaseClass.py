from typing import Any , Dict
from src.exceptions import KeyIsNotInDictionary

class BaseClass():
    def check_type(
        self,
        valid_type: Any,
        value:Any
    ) -> bool:
        return isinstance(value, valid_type)

    def get_data(
        self,
        dictionary: Dict[str, Any],
        key: str
    ) -> Any:
        if key not in dictionary:
            raise KeyIsNotInDictionary(f"{key} is not in dictionary")
        return dictionary[key]
    