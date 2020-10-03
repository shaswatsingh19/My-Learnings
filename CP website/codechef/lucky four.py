# https://www.codechef.com/problems/LUCKFOUR

t = int(input())
for i in range(t):
    n = int(input())
    n = str(n)
    count = 0
    for j in range(len(n)):
        if n[j] == '4':
            count += 1
    print(count)
