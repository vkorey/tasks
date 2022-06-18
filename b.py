def main(n: int, list_of_vacancy: list, k: int, list_of_candidates: list):
    """
    >>> main(2, [['ceo', '1'], ['co_founder', '1']], 3, [['arcady_volozh', 'ceo', '6', '100'], ['elon_musk', 'ceo', '5', '0'], ['ilya_segalovich', 'co_founder', '6', '10']])
    ['arcady_volozh', 'ilya_segalovich']
    >>> main(2, [['plant', '2'], ['gardener', '1']], 5, [['demeter', 'gardener', '4', '12'], ['acacia', 'plant', '0', '5'], ['cactus', 'plant', '0', '1'], ['ficus', 'plant', '0', '4'], ['palm', 'plant', '0', '3']])
    ['cactus', 'demeter', 'palm']
    >>> main(2, [['developer', '2'], ['hacker', '3']], 5, [['anonymous', 'hacker', '6', '0'], ['bjarne_stroustrup', 'developer', '6', '1'], ['julian_assange', 'hacker', '5', '100500'], ['bill_gates', 'developer', '3', '1'], ['guccifer', 'hacker', '2', '0']])
    ['anonymous', 'bill_gates', 'bjarne_stroustrup', 'guccifer', 'julian_assange']
    >>> main(1, [['co_founder', '1']], 3, [['elon_musk', 'co_founder', '6', '200'], ['ilya_segalovich', 'co_founder', '6', '100']])
    ['ilya_segalovich']
    """
    vacancy_dict = {vacancy[0]: int(vacancy[1]) for vacancy in list_of_vacancy}

    dictionary = {}
    result = []
    for vacancy in vacancy_dict.keys():
        temp = []
        for candidate in list_of_candidates:
            if vacancy in candidate:
                temp.append(candidate)
        dictionary[vacancy] = temp

    for k, v in dictionary.items():
        count = vacancy_dict[k]
        dictionary[k] = (sorted(v, key=lambda x: (-(int(x[2])), (int(x[3])))))
        for i in range(count):
            result.append(dictionary[k][i][0])
    return sorted(result)


if __name__ == '__main__':
    import doctest
    failures, errors = doctest.testmod()
