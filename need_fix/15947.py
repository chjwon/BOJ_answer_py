# need fix
# https://www.acmicpc.net/problem/15947


N = int(input())
num = N%14
term = int(N/14)
term += 2
term2 = term -1

# baby sukhwan tu+ru*term tu+ru*(term-1)
# very cute tu+ru*term tu+ru*(term-1)
# in bed tu+ru*term tu+ru*(term-1)
# baby sukhwan
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14

if(num == 1 or num == 13):
    print("baby")
if(num == 2 or num == 14):
    print("sukhwan")
if(num == 5):
    print("very")
if(num == 6):
    print("cute")
if(num == 9):
    print("in")
if(num == 10):
    print("bed")
if(num == 3 or num == 7 or num == 11):
    if(term < 5):
        print('tu'+'ru'*term)
    else:
        print('tu+ru*'+str(term))
if(num == 4 or num == 8 or num == 12):
    if (term2 < 5):
        print('tu' + 'ru' * term2)
    else:
        print('tu+ru*'+str(term2))