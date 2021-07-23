#!/usr/bin/env python3
"""add type annotations to the function"""


from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely get the value"""
    if key in dct:
        return dct[key]
    else:
        return default
