def greedy(num):
    sol = 0
    st = 0
    for item in num:
        if item[0] >= st:
            st = item[1]
            sol += 1
    return sol

num = int(input())
meeting = []
for i in range(num):
    start, end = map(int, input().split())
    meeting.append((start, end))
meeting = sorted(meeting, key = lambda item:item[0]) # 시작 시간 기준으로 정렬
meeting = sorted(meeting, key = lambda item:item[1]) # 종료 시간 기준으로 정렬
print(greedy(meeting))