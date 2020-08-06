def grade(a):
    if(a>89):
        return 'A'
    elif(a>79):
        return 'B'
    elif(a>69):
        return 'C'
    elif(a>59):
        return 'D'
    else:
        return 'F'
a = int(input())
print(grade(a))