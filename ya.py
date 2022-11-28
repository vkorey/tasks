"""
python3 -m doctest <filename>
"""

from collections import Counter
from typing import List


def main(variant: str, original: str) -> List[str]:
    """
    >>> main("A", "A")
    ['correct']
    >>> main("B", "A")
    ['absent']
    >>> main("AB", "AA")
    ['correct', 'absent']
    >>> main("BA", "AB")
    ['present', 'present']
    >>> main("CLEAR", "COVER")
    ['correct', 'absent', 'present', 'absent', 'correct']
    >>> main("AAAA", "ABBA")
    ['correct', 'absent', 'absent', 'correct']
    """
    assert len(variant) == len(original)
    # 1. подсчитать сколько разных букв в оригинальном слове
    cnt = Counter(original)  # {"A": 2, "B": 2}
    result = [''] * len(original)
    # 2. найти все корректные позиции
    for v, o, i in zip(variant, original, range(len(original))):
        if v == o:
            result[i] = 'correct'
            cnt[v] -= 1

    for v, o, i in zip(variant, original, range(len(original))):
        if v == o:
            continue
        # 3. для не корректных позиций показываеть present если есть такая буква
        elif v in cnt and cnt[v] > 0:  # cnt.get(v, 0) > 0
            answer = 'present'
            result[i] = answer
            cnt[v] -= 1
        # 4. в противном случае показывать absent
        else:
            answer = 'absent'
            result[i] = answer
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
