
# https://atcoder.jp/contests/abc162/tasks/abc162_a

n = int(input())
flag = False
while n>0:
    rem  = n%10
    if rem == 7:
        print ("Yes")
        flag = True
        break
    n = n//10
if flag == False:
    print("No")
    
