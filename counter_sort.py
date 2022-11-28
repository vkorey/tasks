def kth_largest(numbers, k):
    """
    python3 -m doctest filename.py

    See https://leetcode.com/problems/kth-largest-element-in-an-array/
    Items are 0 <= i <= 2 ** 8

    >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
    5
    >>> kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    >>> kth_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    9
    >>> kth_largest([10, 9, 5, 6, 4, 7, 2, 1, 3, 8], 3)
    8
    >>> kth_largest([10, 9, 5, 6, 4, 7, 2, 1, 3, 8], 1)
    10
    >>> kth_largest([0, 1, 0, 1, 0, 1, 0, 1], 5)
    0
    >>> kth_largest([256, 256, 255], 3)
    255
    >>> kth_largest([-3, 5, 0, -2, 7, 10], 5)
    -2
    >>> kth_largest([997, 997, 998, 998, 999, 999, 1000, 1001], 5)
    998
    """
    max_item = 2 ** 32  # 4294967296 * 4
    max_item = max(numbers)  # O(n)
    min_item = min(numbers)
    # array.array()
    counter = [0] * (max_item + 1 + abs(min_item))
    # counter = [0, 0, 0, 0, 0]
    for n in numbers:  # O(n)
        i = n - min_item
        counter[i] += 1  # O(1)

    resut = None
    i = len(counter) - 1
    while i > -1:  # O(k)
        v = counter[i]
        if v == 0:
            i -= 1
        else:
            if k <= v:
                return i + min_item
            elif k > v:
                i -= 1
                k -= v


if __name__ == "__main__":
    result = kth_largest([-3, 5, 0, -2, 7, 10], 5)
    print(result)
