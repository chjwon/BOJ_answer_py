# 어렵당

def function_temp(x,y):
    return x*(y+1)

def Area(x,y):
    return function_temp(x,y)+function_temp(y,x)

# 2^31 - 1 = 21 4748 3647


Area_list=[]

# for i in range(1,10):
#     for j in range(1,10):
#         if(i>=j):
#             if (Area(i,j) in Area_list):
#                 pass
#             else:
#                 Area_list.append(Area(i,j))

for i in range(32766,32770):
    for j in range(32766, 32770):
        if(i>=j):
            if (Area(i, j) in Area_list):
                pass
            elif(Area(i,j) < 2147483647):
                Area_list.append(Area(i,j))

Area_list.sort()
print(Area_list)
