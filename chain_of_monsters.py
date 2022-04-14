def main(monsters):
    """
    See https://codeforces.com/contest/1334/problem/C
    >>> main([(7, 15), (2, 14), (5, 3)])
    6
    """
    count = []
    for i in range(len(monsters)):
        next_dmg = 0
        shots = 0
        for i in range(len(monsters)):
            health = monsters[i][0] - next_dmg
            if health > 0:
                shots += health
            next_dmg = monsters[i][1]
        count.append(shots)
        monsters.append(monsters.pop(0))
    return(min(count))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
