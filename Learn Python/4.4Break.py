# The break statement, like in C, breaks out of the innermost enclosing for or while loop.

for i in range(2,10):
    for j in range(2,i):
        if(i%j==0):
            print(i ,"equls ",j ,'*',i//j)
            break
    else:
        print(i," is a prime")


# 2  is a prime
# 3  is a prime
# 4 equls  2 * 2
# 5  is a prime
# 6 equls  2 * 3
# 7  is a prime
# 8 equls  2 * 4
# 9 equls  3 * 3


while True:
    pass # wait for keyboard interaction ctrl+c