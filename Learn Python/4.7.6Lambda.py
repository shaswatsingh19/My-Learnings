# small anynonymus fxn can be created using lambda

# multiple parameter but one experssion
# One is free to use lambda functions wherever function objects are required.

#syntax 
# lambda keyword
# parameters(or bound variable)
# function body

# lambda p1,p2 : expression 


adding = lambda x,y : x+y

print(adding(1,99)) # 100

# The power of lambda is better shown when you use them as an anonymous function inside another function.
def f(n):
    return lambda x : x*n

doubler = f(2)
print(doubler(44))
# no need to change f(n) defination just call f(n)
thipler = f(3) 
print(thipler(5))

quadler  = f(4)

Max = lambda a, b : a if(a > b) else b
 
print(Max(1, 2))