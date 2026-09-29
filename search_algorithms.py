"""Small, testable examples of sorting and binary search."""

from __future__ import annotations


def insertion_sort(values: list[int]) -> list[int]:
    """Return a sorted copy using insertion sort."""
    result = []
    for value in values:
        position = 0
        while position < len(result) and result[position] <= value:
            position += 1
        result.insert(position, value)
    return result


def binary_search(sorted_values: list[int], target: int) -> bool:
    """Find a target in an already sorted list in O(log n) time."""
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        middle = (low + high) // 2
        if sorted_values[middle] == target:
            return True
        if sorted_values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return False


if __name__ == '__main__':
    numbers = [12, 5, 8, 20, 7, 12, 15]
    ordered = insertion_sort(numbers)
    print('ordered:', ordered)
    print('contains 12:', binary_search(ordered, 12))
