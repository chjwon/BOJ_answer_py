year = int(input())
def yun (a):
    if(a%4 == 0):
        if(a%100 == 0):
            if(a%400==0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
print(yun(year))