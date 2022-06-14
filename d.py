n, m = map(int, input().split())
lab = [[j for j in list(input())] for i in range(n)]


def prnt_lab(lab):
    for i in lab:
        print(''.join(i))


def find_start(lab):
    for i in range(len(lab)):
        if "S" in lab[i]:
            for j in range(len(lab[i])):
                if "S" == lab[i][j]:
                    return i, j


def find_ways(lab, i, j):
    # up
    if i >= 1:
        if lab[i-1][j] == ".":
            lab[i-1][j] = "U"
            find_ways(lab, i-1, j)
    # down
    if i <= n-2:
        if lab[i+1][j] == ".":
            lab[i+1][j] = "D"
            find_ways(lab, i+1, j)
    # left
    if j >= 1:
        if lab[i][j-1] == ".":
            lab[i][j-1] = "L"
            find_ways(lab, i, j-1)
    # right
    if j <= m-2:
        if lab[i][j+1] == ".":
            lab[i][j+1] = "R"
            find_ways(lab, i, j+1)


i, j = find_start(lab)
find_ways(lab, i, j)
prnt_lab(lab)
