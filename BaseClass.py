from typing import Any

class BaseClass():
    def check_type(
        self,
        valid_type: Any,
        value:Any
    ) -> bool:
        return isinstance(value, valid_type)