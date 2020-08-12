# 시간 초과
# need fixing
# https://www.acmicpc.net/problem/17479



normal, special, service = map(int, input().split())

NormalMenu={'이름':'가격'}
# normal_price=[]

SpecialMenu={'이름':'가격'}
# special_price=[]

ServiceMenu={'이름':'exist'}
# service_price=[]

for nor in range(normal):
    temp = input().split(' ')
    NormalMenu[temp[0]] = temp[1]

for spe in range(special):
    temp=input().split(' ')
    SpecialMenu[temp[0]] = temp[1]
for ser in range(service):
    temp = input()
    ServiceMenu[temp] = 'exist'

del NormalMenu['이름']
del SpecialMenu['이름']
del ServiceMenu['이름']

# print(NormalMenu)
# print(SpecialMenu)
# print(ServiceMenu)

# order ===========

order = int(input())

NormalPrice = 0
SpecialPrice = 0
ServiceNum = 0

for i in range(order):
    input_menu = input()
    if(input_menu in NormalMenu):
        NormalPrice += int(NormalMenu.get(input_menu))
    if(input_menu in SpecialMenu):
        SpecialPrice += int(SpecialMenu.get(input_menu))
    if(input_menu in ServiceMenu):
        NormalPrice += 1


def solution(total_normal, total_special, total_service):
    if(total_normal >= 20000):
        if(total_special+total_normal >=50000):
            if(total_service <= 1):
                #일반 2만원 이상, 일반 특별 합 5만원 이상, 서비스 1개 이하
                return "Okay"
            else:
                # 일반 2만원 이상, 일반 특별 합 5만원 이상, 서비스 1개 이상
                return "No"
        else:
            if(total_service == 0):
                # 일반 2만원 이상, 일반 특별 합 5만원 미만, 서비스 0개
                return "Okay"
            else:
                # 일반 2만원 이상, 일반 특별 합 5만원 미만, 서비스 1개 이상
                return "No"
    else:
        if(total_special == 0):
            if(total_service==0):
                # 일반 2만원 이하, 특별 0, 서비스 0
                return "Okay"
            else:
                # 일반 2만원 이하, 특별 0, 서비스 1개 이상
                return "No"
        else:
            # 일반 2만원 이하, 특별 있음
            return "No"

print(solution (NormalPrice, SpecialPrice, ServiceNum))