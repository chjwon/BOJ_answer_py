a=int(input()) ; b=int(input()) ; num=[int((b-b%100)/100),int((b%100-b%10)/10),b%10] ; print(a*num[2],a*num[1],a*num[0],a*b,sep='\n')