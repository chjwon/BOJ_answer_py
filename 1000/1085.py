x, y, w, h = map(int, input().split(' '))
distance = [x, y, abs(x - w), abs(y - h)]
print(min(distance))
