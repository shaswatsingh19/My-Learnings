n = int(input())
li = []
second = []
for i in range(n):
    li.append([input(),float(input())])

f = s = -9999
for i in range(len(li)):
    if (f <  li[i][1]):
        s = f
        f = li[i][1]
    elif (s < li[i][1] and li[i][1] != f):
        s = li[i][1]
        second.append(s)
if (s == 999999):
    print("no second element")
else:
    print(second)
