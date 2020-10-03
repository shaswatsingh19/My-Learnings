# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

m,n = input().split()
m = int(m)
n = int(n)
arr =[]
brr = []
for  i in range(m):
    a  = input()
    arr.append(a)
for i in range(n):
    b = input()
    brr.append(b)
arr.sort()
for i in range(m):
    if l[i] == 'a':
        print(i+1,end = " ")
    elif a[i] == 'b':
        print()
        print(i+1,end = " ")
    
    
