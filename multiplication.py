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
    >>> main([1, 2, 0, 5, 0])
    [0, 0, 0, 0, 0]
    >>> main([1, 2, 0, 5, 8])
    [0, 0, 80, 0, 0]
    """
# v1
    """
    result = []
    for i in range(len(numbers)):
        temp_numbers = numbers[:]
        del temp_numbers[i]
        result.append(multiply(temp_numbers))
    return result"""


# v2
    nozeromult = 1
    if len(numbers) == 1:
        return numbers
    if numbers.count(0) > 1:
        return [0 for i in range(len(numbers))]
    elif numbers.count(0) == 1:
        for i in range(len(numbers)):
            if numbers[i] != 0:
                nozeromult *= numbers[i]
                numbers[i] = 0
            elif numbers[i] == 0:
                zero = i
        numbers[zero] = nozeromult
        return numbers
    mult = multiply(numbers)
    for i in range(len(numbers)):
        numbers[i] = int(mult / numbers[i])
    return (numbers)


def multiply(list_):
    n = 1
    for elem in list_:
        n *= elem
    return n


if __name__ == '__main__':
    import doctest
    doctest.testmod()
