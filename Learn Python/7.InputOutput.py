# taking single input 
a = int(input())
b = float(input())
c = input()

# taking multipe input (in string)
m,n,o = input().split()
m = int(m)
n = float(n)
# convert as you will in any type

# You can use map function to map all same type input 
m,n,o = map(int,input().split())

# taking multiple input in list as single line

li = list(map(int,input().split()))


# using string format to output


print("my name is {} and I am {} year old".format("Ajay",23))

# based on index
print("my name is {1} and I am {0} year old".format(24,"Atul"))


print("my name is {name} and I am {age} year old".format(name="Ajay",age=24))

print("%.2f"%(23.2945)) # 2 digit precision 23.29
