t = int(input())
for i in range(t):
    scores = list(map(int,input().split()))
    n = scores[0]
    scores = scores[1:]
    avg = sum(scores)/n
    cnt = len([s for s in scores if s>avg])
    print( "%.3f" % (100*cnt/n), end='%\n' )
