B,C,D=map(int, input().split())

total = 0

burger = input().split(' ')
for i1 in range(B):
    total += int(burger[i1])
    burger[i1] = int(burger[i1])

side = input().split(' ')
for i2 in range(C):
    total += int(side[i2])
    side[i2] = int(side[i2])

water = input().split(' ')
for i3 in range(D):
    total += int(water[i3])
    water[i3] = int(water[i3])

k=min(B,C,D)
burger.sort()
side.sort()
water.sort()

# #
# print(burger)
# print(side)
# print(water)
# #

discount = []
for j in range(k):
    discount.append(burger[B - 1 - j])
    discount.append(side[C - 1 - j])
    discount.append(water[D - 1 - j])

discount_total = 0

for tt in range(3*k):
    discount_total += int(discount[tt])
    # #
    # print('discount list')
    # print(discount[tt])
    # #
    #

discount_total = discount_total * 0.1

# #
# print('discount_total')
# print(discount_total)
# #

print(total)
print(int(total - discount_total))