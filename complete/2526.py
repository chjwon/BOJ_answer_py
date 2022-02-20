N, P = map(int,input().split(' '))
sol = [N]
flag = True
while flag:
    temp = (sol[-1] * N)%P
    if temp not in sol:
        sol.append(temp)
    else:
        answer = sol.index(temp)
        answer = len(sol) - answer
        flag = False
        break
print(answer)