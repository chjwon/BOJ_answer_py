def solution(num):
    sol = 0
    if(num<10):
        sol = num
    elif(num<100):
        sol = num
    elif(num<1000):
        sol=99
        for i in range(100,num+1):
            temp = str(i)
            if(int(temp[0])+int(temp[2]) == 2 * int(temp[1])):
                sol+=1
    elif(num==1000):
        sol=144
    return sol

# main
num = int(input())
print(solution(num))