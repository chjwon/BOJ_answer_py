def hanoi(n,a,b,c): # (n,1,2,3)
    if n==1:
        print(a,c) # (1,3)

    else:
        hanoi(n-1,a,c,b) # (n,1,3,2), n-1개의 원판을 1->2로 옮기는 작업
        print(a,c) # (1,3), 가장 큰 원판 1->3으로 옮기는 작업
        hanoi(n-1,b,a,c) # (n-1,2,1,3), n-1개의 원판을 2->3으로 옮기는 작업
n=int(input())
sum = 1
for _ in range(n-1):
    sum = sum*2 + 1 # n개는 n-1개 행위하고 큰거 옮기고 n-1개 옮기는 방식

print(sum)
hanoi(n,1,2,3)