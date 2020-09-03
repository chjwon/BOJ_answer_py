# 런타임 에러


# 유리근 정리 이용

def if_int(num):
    if(num==int(num)):
        return int(num)
    else:
        return num

def divisor(num,list):
    if(num==0):
        list.append(num)
    elif(num==1):
        list.append(num)
    else:
        for i in (1,int(num/2)):
            if(num%i==0):
                if(i in list):
                    pass
                else:
                    list.append(i)
                if(int(num/i) in list):
                    pass
                else:
                    list.append(int(num/i))


def size(num):
    if(num<0):
        return -num
    else:
        return num


# main
a,b,c,d=map(int,input().split())

list3=[]
list0=[]

divisor(size(a),list3)
divisor(size(d),list0)
# print(list0)
# print(list3)

equation_sol_can=[]

for i in range(len(list3)):
    for j in range(len(list0)):
        temp = list0[j]/list3[i]
        if(temp in equation_sol_can):
            pass
        else:
            equation_sol_can.append(temp)
        if(-temp in equation_sol_can):
            pass
        else:
            equation_sol_can.append(-temp)

# print(equation_sol_can)

solution=[]

def function(a,b,c,d,x):
    return a*(x**3)+b*(x**2)+c*x+d

for pp in range(len(equation_sol_can)):
    if(function(a,b,c,d,equation_sol_can[pp])==0):
        solution.append(equation_sol_can[pp])

for ll in range(len(solution)):
    print("%.4f" %solution[ll])