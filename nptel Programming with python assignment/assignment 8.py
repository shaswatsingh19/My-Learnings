r,m = map(int,input().split())
li = []
li.append(0)

for i in range(r):
    y = int(input())
    li.append(y)

bst = [[0 for z in range(m+1) ] for zz in range(r+1)]

for i in range(1,r+1):
    bst[i][0]  = max(bst[i-1][0] + li[i],li[i])

    for j in range(1,min(i+1,m+1)):
        bst[i][j] = max(bst[i-1][j] + li[i], bst[i-1][j-1])

result = 0
for i in range(1,r+1):
    result  = max(result,bst[i][m])

print(result)
