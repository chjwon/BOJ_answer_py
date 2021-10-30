student = int(input())

score = [0,0,0]
score2 = [0,0,0]
for _ in range(student):
    a,b,c = map(int,input().split(' '))
    score[0] += a
    score[1] += b
    score[2] += c
    score2[0] += a**2
    score2[1] += b**2
    score2[2] += c**2
    
temp = score.index(max(score))
score.sort()
if score[-1] == score[1]:
    temp = score2.index(max(score2))
    score2.sort()
    if score2[-1] == score2[1]:
        temp = -1
print(str(temp+1)+" "+str(score[-1]))