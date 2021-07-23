#!/usr/bin/env python3
"""type-annotated function, make multiplier"""


from typing import Callable
import typing


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def my_multiple(multiple: float) -> float:
        """create new multiple function"""
        return float(multiplier * multiple)

    return my_multiple
