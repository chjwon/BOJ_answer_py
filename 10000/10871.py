N, X = map(int, input().split())
Arr = list(map(int, input().split()))
for i in Arr:
    if i < X:
        print(i, end=" ")