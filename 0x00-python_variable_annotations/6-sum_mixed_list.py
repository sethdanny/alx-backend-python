#!/usr/bin/env python3
'''Module of sum of mixed list of list items'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of mixed numbers"""

    return float(sum(mxd_lst))
