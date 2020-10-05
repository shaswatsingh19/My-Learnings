'''
A*B = 1 so we want to find B which is 
B = 1/A or A(-1) which is multiplicative inverse

and modulo is 

(A*B)%M = 1 ==> Modular Multiplicative inverse
and we  know that B = [1,M-1]

Existence of modular multiplicative inverse :-

An inverse exists only when A and M are coprime i.e GCD(A,M) = 1
'''

# Approach 1: Brute force

def modInverse(A,M):
    A = A % M
    for B in range(1,M):
        if ((A*B)%M) == 1:
            return B

print(modInverse(5,12))
# Time Complexity :- O(M)

# Approach 2: Using Extended Euclidean algorithm
'''
As A and M are coprime which means Ax + My = 1 and the value of x would be
the answer for B
'''
from egcd import  gcdExtended
def modInverseUsingEgcd(A,M):
    g,x,y = gcdExtended(A,M)
    return (x%M+M)%M

print(modInverseUsingEgcd(5,12))

# time complexity :- O(log(max(A,M)))