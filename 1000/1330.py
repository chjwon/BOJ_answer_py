def compare (a,b):
    if (a > b):
        return '>'
    elif (a < b):
        return '<'
    else:
        return '=='

a,b = input().split() ; a= int(a) ; b = int(b)
print(compare(a,b))