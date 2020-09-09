input_list=input().split() ; origin_list=[1,1,2,2,2,8]
for i in range(len(input_list)):
    input_list[i]=int(input_list[i])
    print(origin_list[i]-input_list[i],end=' ')