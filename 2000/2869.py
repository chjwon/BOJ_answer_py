a,b,v = map(int, input().split())
if(int((v-a)/(a-b)) == (v-a)/(a-b)):
    sol = 1 + int((v-a)/(a-b))
else:
    sol = 2 + int((v - a) / (a - b))
print(sol)
print(sol)