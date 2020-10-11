# https://codeforces.com/problemset/problem/231/A

t = int(input())
count = 0
for i in range(t):
    a,b,c = map(int,input().split())
    if (a == b == c ==1) or (a ==b == 1) or (a==c == 1) or (c == b == 1):
        count = count + 1
print(count)
