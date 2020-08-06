sol=0
sol_index=0
for i in range(9):
    a = int(input())
    if(sol<a):
        sol = a
        sol_index =i+1
print(sol)
print(sol_index)