#  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

def sqr(n):
    li = [None]*(n+1)
    for i in range(1,n+1):
        li[i] = i*i
    return li[1:]

li = sqr(30)

print(li[:5] + li[-5:])