def find_last(numbers, first, last):
    if numbers[last] == 1:
        return last
    if last > first:
        middle = first + (last - first) // 2
    if last <= first and numbers[last] != 1:
        return None
    else:
        result = find_last(numbers, middle, last-1)
        if result != None:
            return result
        else:
            return find_last(numbers, 0, middle)

def main(numbers):
    """
    Given a list of zeroes and ones. Find index of the last one.
    When there is no ones in the sequence, return -1
    >>> main([1])
    0
    >>> main([0, 0, 0, 1])
    3
    >>> main([1, 1, 0, 0])
    1
    >>> main([1, 0, 0, 1])
    3
    >>> main([0, 0, 0, 0])
    -1
    """
    if numbers.count(1) == 0:
        return -1
    numbers_lenght = len(numbers)
    first = 0
    last = numbers_lenght - 1
    print(find_last(numbers, first, last))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
