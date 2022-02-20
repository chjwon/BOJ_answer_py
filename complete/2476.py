people = int(input())
sol = 0
for _ in range(people):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        sol = max(sol, 10000+a*1000)
    elif a == b:
        sol = max(sol, 1000+a*100)
    elif a == c:
        sol = max(sol, 1000+a*100)
    elif b == c:
        sol = max(sol, 1000+b*100)
    else:
        sol = max(sol, 100 * max(a,b,c))
print(sol)