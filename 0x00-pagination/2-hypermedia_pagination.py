#!/usr/bin/env python3
"""index range"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """define func"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """define func"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start: end] if len(data) > start else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """define func"""
        data = self.get_page(page, page_size)
        data_len = len(self.dataset())
        total_page = (data_len + (page_size - 1))  // page_size
        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_page else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_page 
                }
