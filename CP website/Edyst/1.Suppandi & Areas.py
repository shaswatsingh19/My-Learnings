#rectangle = > square
#square => triangle
#triangle => rectangle
#else => 0

def square(a):
    return a*a

def triangle(a,b):
    ans = (a*b)/2
    return int(ans)

def rectangle(a,b):
    return a*b

def area(shape,a,b):
    if shape == 'rectangle':
        print(square(a))
    elif shape == 'square':
        print(triangle(a,b))
    elif shape == 'triangle':
        print(rectangle(a,b))
    else:
        print(0)


t = int(input())
for i in range(t):
    shape = input()
    a = int(input())
    b = int(input())
    area(shape,a,b)
