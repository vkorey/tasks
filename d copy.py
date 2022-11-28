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
    left_border, right_border = 1, m-2
    top_border, bottom_border = 1, n-2
    next_steps = [(i, j, "S")]
    while next_steps:
        i, j, mark = next_steps.pop()
        lab[i][j] = mark

        # up
        if i >= top_border:
            if lab[i-1][j] == ".":
                step = (i - 1, j, "U")
                next_steps.append(step)
        # down
        if i <= bottom_border:
            if lab[i+1][j] == ".":
                step = (i + 1, j, "D")
                next_steps.append(step)
        # left
        if j >= left_border:
            if lab[i][j-1] == ".":
                step = (i, j - 1, "L")
                next_steps.append(step)
        # right
        if j <= right_border:
            if lab[i][j+1] == ".":
                step = (i, j + 1, "R")
                next_steps.append(step)


i, j = find_start(lab)
find_ways(lab, i, j)
prnt_lab(lab)
