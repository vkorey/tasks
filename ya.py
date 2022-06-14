sm = [
    ['ceo', '1'],
    ['co_founder', '1']
]
js = [
    ['arcady_volozh', 'ceo', '6', '100'],
    ['elon_musk', 'ceo', '5', '0'],
    ['ilya_segalovich', 'co_founder', '6', '10']
]

for name, vac_sum in sm:
    answer = []
    for cand in js:
        if name in cand:
            answer.append(cand)
    for a

    print(answer)
