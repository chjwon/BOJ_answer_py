import sys
from itertools import combinations

input = sys.stdin.readline

temp = True

while temp:
    numbers = list(map(int, input().strip().split()))
    n = int(numbers[0])
    if (n == 0):
        temp = False
        break
    for i in combinations(numbers[1:], 6):
        print(' '.join(map(str, i)))
    print()
