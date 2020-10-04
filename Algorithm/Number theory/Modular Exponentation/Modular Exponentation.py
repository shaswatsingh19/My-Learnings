# In python we use pow() function to use fast exponentiation
# pow(x,e,m)
# will provide the same result

'''
Algorithm:
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