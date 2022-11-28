from typing import List

def main(numbers: List[int]) -> bool:
    """
    We need a function which checks a sequence of numbers.
    It should return True only when every next number is greater
    than the previous one.
    >>> main([1, 2, 3])
    True
    >>> main([1, 3, 2])
    False
    >>> main([2, 3, 1])
    False
    >>> main([1, 2, 3, 4])
    True
    >>> main([1, 2, 3, 4, 8, 15, 26, 99])
    True
    >>> main([1, 0, 3, 4, 8, 15, 26, 99])
    False
    >>> main([0, 1])
    True
    """
    if len(numbers) == 2:
        return True if  numbers[0] < numbers[1] else False
    if len(numbers) == 3:
        return True if numbers[0] < numbers[1] and numbers[1] < numbers[2] else False
    mid = len(numbers) // 2
    left = main(numbers[:mid+1])
    right = main(numbers[mid-1:])
    return left and right
