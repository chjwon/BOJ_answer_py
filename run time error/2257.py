# runtime error??



def solution(string):
    solo = 0
    if 'H' in string:
        indexH = string.index('H')
        if len(string) - 1 < indexH + 2:
            solo += 1
        elif string[indexH + 2] == '(':
            solo += 1
        else:
            solo += int(string[indexH + 2]) * 1

    if 'O' in string:
        indexO = string.index('O')
        if len(string) - 1 < indexO + 2:
            solo += 16
        elif string[indexO + 2] == '(':
            solo += 16
        else:
            solo += int(string[indexO + 2]) * 16

    if 'C' in string:
        indexC = string.index('C')
        if len(string) - 1 < indexC + 2:
            solo += 12
        elif string[indexC + 2] == '(':
            solo += 12
        else:
            solo += int(string[indexC + 2]) * 12

    return solo


chemistry = input()
print(solution(chemistry))
