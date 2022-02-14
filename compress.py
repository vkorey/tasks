def compress_string(text):
    """
    Write a function which will "compress" input string.
    Instead of repeating a char there should be just number of repetitions.
    >>> compress_string('aaabbbbcddd')
    'a3b4cd3'
    >>> compress_string('abcdefgh')
    'abcdefgh'
    >>> compress_string('aaaaabaaaaa')
    'a5ba5'
    >>> compress_string('aaaaaaaaaab')
    'a10b'
    >>> compress_string('')
    ''
    """
    if text == '':
        return ''
    result = text[0]
    count = 1
    for char in text[1:]:
        if char == result[-1]:
            count += 1
        else:
            if count == 1:
                result += char
            else:
                result += str(count) + char
            count = 1

    if count != 1:
        result += str(count)
    return result


def decompress_string(text):
    """
    Write a inverse function.
    >>> decompress_string('')
    ''
    >>> decompress_string('a10b')
    'aaaaaaaaaab'
    >>> decompress_string('a5ba5')
    'aaaaabaaaaa'
    >>> decompress_string('a3b4cd3')
    'aaabbbbcddd'
    """
    num = ''
    result = ''
    for char in text:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                result += (result[-1] * (int(num)-1)) + char
                num = ''
            else:
                result += char
    if num != '':
        result += (result[-1] * (int(num)-1))
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
