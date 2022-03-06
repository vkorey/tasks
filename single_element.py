def main(numbers):
    """
    See https://leetcode.com/problems/single-element-in-a-sorted-array/

    You are given a sorted array consisting of only integers where
    every element appears exactly
    twice, except for one element which appears exactly once.
    Find this single element that appears
    only once.

    Follow up: Your solution should run in O(log n) time and O(1) space.

    >>> main([1, 1, 2, 3, 3, 4, 4, 8, 8])
    2
    >>> main([3, 3, 7, 7, 10, 11, 11])
    10
    >>> main([])
    >>> main([1])
    1
    >>> main([1, 1, 2])
    2
    """
    result = 0
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 3:
        return numbers[2]
    i = 0
    while i < len(numbers):
        if numbers[i] == numbers[i+1]:
            i += 2
        else:
            return numbers[i]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
