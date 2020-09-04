s = input()
for a in 'abcdefghijklmnopqrstuvwxyz':
    try:
        print(s.index(a), end=' ')
    except:
        print(-1, end=' ')