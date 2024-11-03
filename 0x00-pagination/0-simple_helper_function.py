#!/usr/bin/env python3
"""index range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """define func"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
