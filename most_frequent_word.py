def most_frequent_word(text):
    """
    >>> most_frequent_word('i think therefore i am')
    'i'
    >>> most_frequent_word("be the change that you wish to see in the world")
    'the'
    """
    count = 0
    most_frequent = 1
    text_list = text.split(' ')
    for word in text_list:
        word_count = text.count(word)
        if most_frequent < word_count:
            result = count
            most_frequent = word_count
        count += 1
    return text_list[result]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
