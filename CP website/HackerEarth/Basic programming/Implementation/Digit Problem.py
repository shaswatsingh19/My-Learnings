PROBLEM

[PROBLEM LINK](https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/)

PROBLEM STATEMENT

This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.

Input:

First line of the input contains two integers X and K separated by a single space.

Output:

Print the largest number formed in a single line.

Constraints:
    1 <= X <= 10^18
    0 <= K <= 9
    
SAMPLE INPUT :  4483 2
SAMPLE OUPTUT : 9983

Explanation:
First two digits of the number are changed to get the required number.


SOLUTION :


a,b = input().split()
i = 0 
b  = int(b)
while b:
    if a[i] != '9':
        a   = a.replace(a[i],'9',1)
        b = b - 1
    i = i + 1
print(a)
