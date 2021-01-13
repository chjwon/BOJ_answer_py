def change(inp):
    if inp[0]=='E':
        inp='I'+inp[1:]
    else:
        inp='E'+inp[1:]

    if inp[1]=='S':
        inp=inp[0]+'N'+inp[2:]
    else:
        inp=inp[0]+'S'+inp[2:]

    if inp[2]=='T':
        inp=inp[0:2]+'F'+inp[3]
    else:
        inp=inp[0:2]+'T'+inp[3]

    if inp[3]=='J':
        inp=inp[0:3]+'P'
    else:
        inp=inp[0:3]+'J'
    return inp

print(change(input()))