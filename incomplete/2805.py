N_tree , N_meter = map(int, input().split(' '))
total = 0
tree = input().split(' ')
for i in range(N_tree):
    tree[i] = int(tree[i])
    total += tree[i]
# print(tree, total)
ans=0
while(1):
    ans+=1
    total=0
    for i in range(N_tree):
        tree[i]-=1
        if tree[i] > 0:
            total += tree[i]
    if total < N_meter:
        print(ans-1)
        break
    else:
        pass