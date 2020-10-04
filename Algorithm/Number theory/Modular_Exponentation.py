# In python we use pow() function to use fast exponentiation
# pow(x,e,m)
# will provide the same result

# Basic Method 
# we just use pow(x,e) and that it but basic recursive and iterative algorithm

def recursivePower(x,e):
    
    if e == 0:
        return 1
    return x*recursivePower(x,e-1)

# We can also use iterative approach 

def iterativePower(x,e):
    ans = 1
    while e>0:
        ans = ans*x
        e = e-1
    return ans

'''
The above time complexity is O(n) but
if we use large number like 10**19 it should be very  very slow
thats why we use O(logn) approach
'''
'''
Optimized method
Here :-
x = Base
y = Exponent
m = 1e9+7 or 1000000007
'''
def f(x,e,m):
    y = 1
    while e>0:
        if x%2 == 0:
            x = (x*x)%m
            e = e//2
        else:
            y = (x*y)%m
            e = e - 1
    return y
print(f(1233232,212344,1e9+7))
236644787
