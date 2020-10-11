# https://www.codechef.com/COW42020/problems/COW3G

def find_lcm(num1,num2):
    if num1>num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num%den
    while rem!= 0:
        num= den
        den = rem
        rem = num%den
    gcd = den
    lcm = int(int(num*num2)/int(gcd))
    return lcm

n = int(input())
print()
arr = list(map(int,input().split()))
num1 = arr[0]
num2 = arr[1]
lcm = find_lcm(num1,num2)

for i in range(2,len(arr)):
    lcm = find_lcm(lcm,arr[i])
print(lcm)
