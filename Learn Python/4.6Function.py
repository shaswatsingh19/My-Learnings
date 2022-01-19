def sum(a,b):
    """Function to print sum"""
    return a+b


print(sum.__doc__) # docstring (optional)
# Function to print sum

print(sum(2,5)) # 7

# The execution of a function introduces a new symbol table used for the local variables of the function.
# Whereas variable references first look in the local symbol table => 
# local symbol tables of enclosing functions, 
# then in the global symbol table, 
# finally in the table of built-in names. 
# Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement), although they may be referenced.

# even functions without a return statement do return a value. This value is called None (it’s a built-in name). 


# Default parameter 
def minus(a=0,b=0):
    '''Minus of two values'''
    return a-b

print(minus()) # 0
print(minus(5,1)) # 4

def f(a, L=[]):
    L.append(a)
    return L 

print(f(1)) # [1]
print(f(2)) #[1, 2]
print(f(3))  #[1, 2, 3]

# Defualt value is evaluated only once

def f(a, L=None):
    if L is None:
        L = [] 
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2,[])) # [2] here new [] will go as the if condition work that does not make a new []
