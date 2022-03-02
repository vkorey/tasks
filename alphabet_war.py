"""
See https://www.codewars.com/kata/alphabet-war

== Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters
and right side letters was too high and the war began.

== Task
Write a function that accepts fight string consists of only small letters and
return who wins the fight. When the left side wins return Left side wins!,
when the right side wins return Right side wins!,
in other case return Let's fight again!.

The left side letters and their power:
w - 4
p - 3
b - 2
s - 1

The right side letters and their power:
m - 4
q - 3
d - 2
z - 1

The other letters don't have power and are only victims.
"""
from collections import Counter


def fight(text):
    """
    >>> fight('')
    "Let's fight again!"
    >>> fight('Fddsdfg')
    "Let's fight again!"
    >>> fight('abracadabra')
    'Left side wins!'
    >>> fight('z')
    'Right side wins!'
    >>> fight('zdqmwpbs')
    "Let's fight again!"
    >>> fight('zzzzs')
    'Right side wins!'
    >>> fight('wwwwwwz')
    'Left side wins!'
    """

    if text == '' or text.islower() is False:
        return "Let's fight again!"
    counter = Counter(text)
    left = ((counter['w'] * 4) +
            (counter['p'] * 3) +
            (counter['b'] * 2) +
            (counter['s'] * 1)
            )
    right = ((counter['m'] * 4) +
             (counter['q'] * 3) +
             (counter['d'] * 2) +
             (counter['z'] * 1)
             )

    if left > right:
        return "Left side wins!"
    elif left < right:
        return "Right side wins!"
    else:
        return "Let's fight again!"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
