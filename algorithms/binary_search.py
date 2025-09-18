"""
Binary Search Algorithm Implementation

This module contains a class-based implementation of binary search.
"""

import time

class BinarySearch:
    """
    Binary search algorithm.

    Efficient searching in sorted sequences with O(log n) time complexity.

    Args:
        arr: A sorted list of elements. The list MUST be sorted in ascending order.
    """
    
    def __init__(self, arr: list[int]) -> None:
        """
        Initialize the BinarySearch with a sorted array.
        
        Args:
            arr: A sorted list of integers in ascending order.
        """
        self.arr = arr
        self.last_time_ms = 0
        self.last_iterations = 0

    def search(self, target: int) -> int:
        """
        Search for a target element in the sorted array.

        Args:
            target: The element to search for.

        Returns:
            The index of the target element if found, otherwise -1.
        """
        if not self.arr:  # or len(self.arr) == 0
            self.last_time_ms = 0
            self.last_iterations = 0
            return -1
        
        start = time.perf_counter()
        iterations = 0
        l, r = 0, len(self.arr) - 1
        while l <= r:
            iterations += 1
            m = (l + r) // 2
            if self.arr[m] == target:
                end = time.perf_counter()
                self.last_time_ms = (end - start) * 1000  # Convert to milliseconds
                self.last_iterations = iterations
                return m
            if self.arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        end = time.perf_counter()
        self.last_time_ms = (end - start) * 1000  # Convert to milliseconds
        self.last_iterations = iterations
        return -1

    def get_last_time_ms(self) -> float:
        return self.last_time_ms

    def get_last_iterations(self) -> int:
        return self.last_iterations

    def performance_report(self) -> None:
        print("Execution time: ", self.last_time_ms, "ms")
        print("Iterations: ", self.last_iterations)
        