alphaNum = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
numAlpha = {1: 'A', 2:'B' , 3: 'C', 4: 'D', 5:'E' , 6:'F' , 7: 'G', 8: 'H'}



def oneMove(present, moving):
    if moving == 'R':
        if present[0] != 8:
            present += 1

    elif moving == 'L':
        if present[0] != 1:
            present -= 1

    elif moving == 'B':
        if present[1] != 1:
            present -= 1

    elif moving == 'T':
        if present[1] != 8:
            present += 1

    return present, moving


def twoMoving(present, moving):
    if moving[0] == 'R':
        if present[0] != 8:
            present += 1

    elif moving[0] == 'L':
        if present[0] != 1:
            present -= 1

    if moving[1] == 'B':
        if present[1] != 1:
            present -= 1

    elif moving[1] == 'T':
        if present[1] != 8:
            present += 1

    return present, moving


def moveit(present, moving):
    present[0] = str(alphaNum[present[0]])
    # vert = int(present[1])
    if len(moving) == 1:
        present, moving = oneMove(present, moving)
    elif len(moving) == 2:
        present, moving = twoMoving(present, moving)
    return present

# main
king, rock, num = input().split(' ')
move = int(num)
move_list = []
for _ in range(move):
    temp = input()
    move_list.append(temp)
    king = moveit(king,temp)

print(king)
# print(king, rock, move, move_list)
# rock이 어떻게 움직인다고...?
