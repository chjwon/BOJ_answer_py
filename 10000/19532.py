
list=input().split()
for i in range(len(list)):
    list[i]=int(list[i])
list_1 = [list[4]*list[0],list[4]*list[1],list[4]*list[2]]
list_2 = [list[1]*list[3],list[1]*list[4],list[1]*list[5]]
sol_x_list = [list[4]*list[0]-list[1]*list[3],list[4]*list[2]-list[1]*list[5]]
list_3=[list[3]*list[0],list[3]*list[1],list[3]*list[2]]
list_4=[list[0]*list[3],list[0]*list[4],list[0]*list[5]]
sol_y_list=[list[3]*list[1]-list[0]*list[4],list[3]*list[2]-list[0]*list[5]]
print(str(int(sol_x_list[1]/sol_x_list[0]))+' '+str(int(sol_y_list[1]/sol_y_list[0])))



# 런타임 에러 뜸
# 모듈을 사용한 풀이

# import numpy as np
# list=input().split()
# for i in range(len(list)):
#     list[i]=int(list[i])
# A=np.array([[list[0],list[1]],[list[3],list[4]]])
# B=np.array([list[2],list[5]])
# C=np.linalg.solve(A,B)
# print(int(C[0]),end=' ')
# print(int(C[1]))
