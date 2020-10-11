# https://codeforces.com/problemset/problem/282/A

n= int(input())
x = 0
for i in range(n):
    s = input()
    if s == '++X' or s == 'X++':
        x = x + 1
    elif s == '--X' or s == 'X--':
        x = x -1
print(x)
