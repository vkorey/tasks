from tkinter.messagebox import NO


def find_single(numbers, first, last):
    if first >= last:
        return -1
    if first < last:
        middle = (first + last) // 2
    if numbers[middle] != numbers[middle - 1] and numbers[middle] != numbers[middle + 1]:
        return numbers[middle]
    elif numbers[middle] != numbers[middle - 1]:
        find_single(numbers, first, middle - 2)
    else:
        find_single(numbers, middle + 2, last)
    

def main(numbers):
    """
    See https://leetcode.com/problems/single-element-in-a-sorted-array/

    You are given a sorted array consisting of only integers where
    every element appears exactly
    twice, except for one element which appears exactly once.
    Find this single element that appears
    only once.

    Follow up: Your solution should run in O(log n) time and O(1) space.

    >>> main([1, 1, 2, 3 ,3, 4, 4, 8, 8])
    2
    >>> main([3, 3, 7, 7, 10, 11, 11])
    10
    >>> main([])
    >>> main([1])
    1
    >>> main([1, 1, 2])
    2
    """
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    elif numbers[0] != numbers[1]:
        return numbers[0]
    elif numbers[len(numbers) - 1] != numbers[len(numbers) - 2]:
        return numbers[len(numbers) - 1]
 
    print(find_single(numbers,0,len(numbers) - 1))



if __name__ == '__main__':
    import doctest
    doctest.testmod()
