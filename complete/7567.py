def tenFive(str1, str2):
    if str1 == '(':
        if str2 == '(':
            return 5
        else:
            return 10
    if str1 == ')':
        if str2 == ')':
            return 5
        else:
            return 10
inputStr = input()
sol = 10
for i in range(len(inputStr)-1):
    sol += tenFive(inputStr[i],inputStr[i+1])
print(sol)