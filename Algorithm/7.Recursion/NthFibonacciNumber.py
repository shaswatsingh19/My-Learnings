'''
Given a number N. Print the Fibonacci number of N.

'''
# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')
# from itertools import permutations as p
# from itertools import combinations as c


def fib(n):
	s =0
	if  n ==1:
		s +=0
		return 0
	elif n==2:
		s+=1
		return 1
	else:
		return fib(n-1)+fib(n-2)

t   = int(input())
print(fib(t))

'''
Input:
5
Output:
3

Input:
1
Output:
0



'''