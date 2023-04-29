def vps(inputstr:list):
    sol = 0
    for i in inputstr:
        if i == "(":
            sol += 1
        elif i == ")" and sol == 0:
            return False
        else:
            sol -= 1
        
    if sol == 0:
        return True
    else:
        False
        
        
num = int(input())
for _ in range(num):
    inputstr = list(input())
    if vps(inputstr):
        print('YES')
    else:
        print("NO")