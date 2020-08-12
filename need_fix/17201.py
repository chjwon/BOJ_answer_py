# need fix
# https://www.acmicpc.net/problem/17201

length = int(input())
chain = str(input())
mag = []
temp = 0
for sep in range(length):
    mag.append(chain[temp:temp+2])
    temp +=2
    # mag[sep] = int(mag[sep])


# print(mag)

def swap(a,b):
    a,b = b,a


def mag_chain (mag, length):
    for i in range(length - 1):
        if(mag[i][1] == mag[i+1][0]):
            return 'No'
        return 'Yes'

print(mag_chain(mag,length))