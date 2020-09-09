# 시간 초과
# https://m.blog.naver.com/PostView.nhn?blogId=thnam91&logNo=220998019103&proxyReferer=https:%2F%2Fwww.google.com%2F


import operator as op
from functools import reduce

def nCr(n,r):
    if(n<1 or r<0 or n<r):
        raise ValueError
    r=min(r,n-r)
    numerator = reduce(op.mul, range(n,n-r,-1),1)
    denominator = reduce(op.mul,range(1,r+1),1)
    return numerator//denominator

n,r,num=map(int,input().split())
print(nCr(n,r)%num)