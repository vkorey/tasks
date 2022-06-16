class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return False
        self.stack.pop()

    def size(self):
        return len(self.stack)


def main(text: str):
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
    """

    s = Stack()
    text = list(text)

    error_counter = 0
    for char in text:
        if char == '(':
            s.push(char)
        elif char == ')':
            if s.pop() is False:
                error_counter += 1

    stack_size = s.size()

    if error_counter == 1:
        return (text.index(')') + 1)
    elif stack_size == 1:
        return (text.index('(') + 1)
    else:
        return -1


if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
