def most_frequent_word(text):
    """
    >>> most_frequent_word('i think therefore i am')
    'i'
    >>> most_frequent_word("be the change that you wish to see in the world")
    'the'
    >>> most_frequent_word("")
    ''
    """
    if text == '':
        return ''
    most_frequent = 1
    text_list = text.split(' ')
    for word in text_list:
        word_count = text.count(word)
        if most_frequent < word_count:
            result = word
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
