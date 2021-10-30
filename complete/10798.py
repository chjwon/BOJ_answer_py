inputStr = [[0] * 15 for i in range(5)]
for i in range(5):
    tempStr = list(input())
    tempStr_len = len(tempStr)
    for j in range(tempStr_len):
        inputStr[i][j] = tempStr[j]
for i in range(15):
    for j in range(5):
        if inputStr[j][i] == 0:
            continue
        else:
            print(inputStr[j][i], end='')