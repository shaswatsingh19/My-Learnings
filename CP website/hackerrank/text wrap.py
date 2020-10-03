# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap
s =input()
n =int(input())
'''
for i in range(0,len(s),n):
    print(s[i:i+n])
'''
print(textwrap.wrap(s,n))
print(textwrap.fill(s,n))
