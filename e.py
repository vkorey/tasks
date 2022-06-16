from typing import List


def main(input_string: str) -> List[str]:
    """
    >>> main("a + b = b + a =")
    -1
    """
    input_string = list(input_string)
    if "(" or ")" not in input_string:
        return -1
    n = 0

    eq = find_eq(input_string)

    for i in input_string[::eq]:
        scob_count = 0
        if input_string[i] == '(':
            scob_count += 1
        if input_string[i] == ')':
            scob_count -= 1
    
    

    if "=" in input_string:
        while n < len(input_string):
            pass


def get_sequence(input_string):
    pass


def find_eq(input_string) -> int:
    return input_string.index('=')
