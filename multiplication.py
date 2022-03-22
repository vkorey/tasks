def main(numbers):
    """
    Given a sequence of integers.
    Build a new sequence of the same length.
    Each element of a new sequence should be calculated
    as a multiplication of elements of the original sequence except
    the element with the same index.  Think about possible corner cases.
    >>> main([1, 5, 3])
    [15, 3, 5]
    >>> main([1, 2, 2, 5, 8])
    [160, 80, 80, 32, 20]
    """
    result = []
    for i in range(len(numbers)):
        temp_numbers = numbers[:]
        del temp_numbers[i]
        result.append(multiply(temp_numbers))
    return result


def multiply(list_):
    n = 1
    for elem in list_:
        n *= elem
    return n


if __name__ == '__main__':
    import doctest
    doctest.testmod()
