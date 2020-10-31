from decimal import *
import math
getcontext()
getcontext().prec = 14
a,b,c = map(Decimal, input().split())
s=(a+b+c)/2
S=Decimal(str(math.sqrt(s*(s-a)*(s-b)*(s-c))));
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(a*b*c/(4*S))
print(2*S/(a+b+c))
d=(a*b*c/(4*S)-(4*S/(a+b+c)))
if d<=0 :
    d=0
else :
    d=math.sqrt(a*b*c/(4*S)*d)
print(d)
print(a*b*c/(4*S)+2*S/(a+b+c))







"""
import math

# 틀린 풀이
def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def ex_rad(a, b, c):
    return (a * b * c) / (area(a, b, c) * 4)


def in_rad(a, b, c):
    return 2 * area(a, b, c) / (a + b + c)


def exin_dis(a, b, c):
    R = ex_rad(a, b, c)
    r = in_rad(a, b, c)
    if R >= 2 * r:
        return math.sqrt(R*(R-2*r))
    else:
        return 0


def es_dis(a, b, c):
    return ex_rad(a, b, c) + in_rad(a, b, c)


tri1, tri2, tri3 = map(int, input().split(' '))
print(area(tri1, tri2, tri3))
print(ex_rad(tri1, tri2, tri3))
print(in_rad(tri1, tri2, tri3))
print(exin_dis(tri1, tri2, tri3))
print(es_dis(tri1, tri2, tri3))
"""
