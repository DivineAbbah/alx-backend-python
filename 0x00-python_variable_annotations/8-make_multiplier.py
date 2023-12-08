#!/usr/bin/env python3
""" Complex Funtions types"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    params:  float multiplier as argument,
    returns  function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        """ multiplies the float by multiplier """
        return float(n * multiplier)

    return f
