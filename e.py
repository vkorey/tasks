class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return False
        return self.stack.pop()

    def size(self):
        return len(self.stack)


def main(text: str) -> int:
    """
    >>> main("a + b = b + a")
    -1
    >>> main("d + (a + (b + c) = (a + b) + c + d")
    5
    >>> main("(a((b + c) = ab + bc")
    -1
    >>> main(")a((b + c)) = ab + bc")
    1
    >>> main("(s))a((b + c)) = ab + bc")
    3
    >>> main(")b + c = ab + bc")
    1
    >>> main(")b + (c = ab + (bc)")
    -1
    >>> main("(((b + (c))))) = ab + (bc)")
    10
    """
    brackets = []
    for i , char in enumerate(text):
        if char == '(' or char == ')':
            item = char, i
            brackets.append(item)
    s = Stack()
    result = None
    error_counter = 0
    for j, (char, i) in enumerate(brackets):
        if char == '(':
            s.push(i)
        elif char == ')':
            if s.pop() is False:
                error_counter += 1
                if result is None:
                    result = j

    stack_size = s.size()

    if error_counter == 1 and stack_size == 0:
        while result > 0:
            if brackets[result][0] != brackets[result - 1][0]:
                break
            result -= 1
        return brackets[result][1] + 1
    elif stack_size == 1 and error_counter == 0:
        return (s.pop()  + 1)
    else:
        return -1


if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
