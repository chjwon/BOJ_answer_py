def func(a):
    # 대각선이 만나려면 2개의 대각선 필요
    #2개 대각선 필요하면 4개의 점이 필요
    #n개의 점중에 4개의 점을 선택
    return int(a*(a-1)*(a-2)*(a-3)/24)
n=int(input())
print(func(n))