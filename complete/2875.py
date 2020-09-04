import sys
woman, man, remain = map(int,input().split(' '))
team = woman//2 if woman//2 < man else man
ans = 0
for t in range(team, -1, -1):
    if woman - 2*t + man - t >= remain:
        ans = t
        break
sys.stdout.write(str(ans))




# 흠 수정 시도해됨
# team = woman//2 if woman//2 < man else man
# team = team if woman+man-3*team>=remain else team-int((remain-(woman+man-3*team))/3)-1 ; print(team)
