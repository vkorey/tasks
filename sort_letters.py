from collections import Counter


def sort_letters(text):
    """
    python3 -m doctest <filename>

    Return a string of the same letters where all the letters are sorted by
    its frequency in descending order. In case of equal frequency letters
    should go in the order they were met in the original string.
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    """
    # 1. count all letters
    count_letters = Counter(text)  # O(n)

    # 2. starting from the most frequent letter
    pairs = count_letters.items()  # O(m)
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)  # O(m * ln(m))
    # print(sorted_pairs)
    result = []
    #  - repeat letter several times
    for letter, freq in sorted_pairs:  # O(m)
        result.append(letter * freq)  # O(1)
    # 3. combine result
    # print(result)
    return ''.join(result)  # O(m * ln(m) + 3 * m + n)


def sort_letters_2(text):
    """
    python3 -m doctest <filename>

    Return a string of the same letters where all the letters are sorted by
    its frequency in descending order. In case of equal frequency letters
    should go in the order they were met in the original string.
    >>> sort_letters_2('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters_2('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters_2('aba')
    'aab'
    >>> sort_letters_2('abcabccba')
    'aaabbbccc'
    """
    # 1. count all letters
    count_letters = Counter(text)  # O(n)
    # advanced py3.6
    index_by_letter = {}
    for i, letter in enumerate(text):  # O(n)
        if letter not in index_by_letter:
            index_by_letter[letter] = i

    # 2. starting from the most frequent letter
    pairs = count_letters.items()  # O(m)

    reversed_pairs = [(f, -index_by_letter[l], l) for l, f in pairs]  # O(m)
    sorted_pairs = sorted(reversed_pairs, reverse=True)  # O(m * ln(m))
    result = []
    #  - repeat letter several times
    for freq, _, letter in sorted_pairs:  # O(m)
        result.append(letter * freq)  # O(1)
    # 3. combine result
    return ''.join(result)  # O(m * ln(m) + 3 * m + n)
