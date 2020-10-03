# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/
'''
t = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(t):
    print(a[i] + b[i] ,end= " ")
'''

t = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(" ".join(map(str,[a[i]+b[i] for i in range(t)])))
