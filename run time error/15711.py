def primes_up_to_good(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]

def solution(num):
    list = primes_up_to_good(num - 2)
    n = len(list)
    # 2 + 소수인 경우
    if num % 2==0:
        return 'YES'
    elif list[n-1] == (num-2) :
        return 'YES'
    else:
        return 'NO'


input_num = int(input())
for _ in range(input_num):
    a,b = map(int,input().split(' '))
    print(solution(a+b))