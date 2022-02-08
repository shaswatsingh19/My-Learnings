'''
Given a number N. Print the Fibonacci number of N.
We now store values of all the previous fibonacci numbers 
and store in a dictonary
'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


def  fib(n,m={1:0,2:1}):
	if n in m:
		return m[n]
	else:
		m[n] = fib(n-1,m)+fib(n-2,m)
		return m[n]
    
t = int(input())
print(fib(t))


'''
O(n) time and O(n) space complexity

Input:36
Output:9227465

Input:100
Output:218922995834555169026

Input:500
Output:86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501



'''