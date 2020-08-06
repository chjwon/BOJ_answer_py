a,b = input().split();a=int(a);b=int(b)
if(b<45):
    b+=60
    a-=1
if(a<0):
    a+=24
print(str(a)+' '+str(b-45))