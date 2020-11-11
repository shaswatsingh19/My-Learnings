'''
Write a program to cyclically rotate an array by one.

'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

#code
t = int(input())
while t:
    n = int(input())
    arr = list(map(int,input().split()))
    print(arr[-1],end=' ')
    for i in range(n-1):
        print(arr[i],end=' ')
    print()
    t-=1