def solve(day, TimeList, PayList):

    solution = 0
    for i in range(0,1<<day):
        d=day # 남은 퇴사일
        result = 0
        counsel_day = 0
        for j in range(0,day):
            if(i&(1<<j)):
                # 상담 끝
                if(counsel_day==0):
                    # 남은 퇴사일과 상담시 걸리는 시간 비교
                    if(d>=TimeList[j]):
                        counsel_day = TimeList[j]
                        result +=PayList[j]

            if(counsel_day>0):
                # 하루 상담 진행
                counsel_day -=1
            d-=1 # 하루 흘러감
        if(solution<result):
            solution=result
    return solution


day = int(input())
TimeList=[]
PayList=[]
for _ in range(day):
    temp1,temp2 = map(int, input().split())
    TimeList.append(temp1)
    PayList.append(temp2)
print(solve(day,TimeList,PayList))