num=int(input())
test=[]
sol=[0,1,2,4,7,13,24,44,81,149,274,504]
for _ in range(num):
    test.append(int(input()))
# print(test)
for i in range(num):
    print(sol[test[i]])

# 점화식은 f(t)=f(t-1)+f(t-2)+f(t-3)