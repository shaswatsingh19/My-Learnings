# https://practice.geeksforgeeks.org/contest-problem/m-and-n5047/0/



def count(li):
    m = li[0]
    n = li[1]
    sum_of_li = sum(li)
    temp = n
    count  = 0
    while n>1:
        rem = n%10
        count = count + 1
        n = n/10
    temp1 = sum_of_li
    count1 = 0 
    while sum_of_li > 1:
        rem = sum_of_li % 10
        count1 =count1 + 1
        sum_of_li = sum_of_li /10
    if count == count1:
        print(temp)
    else:
        print(temp1)


t  = int(input())
for  i in range(t):
    li= list(map(int,input().split()))
    count(li)
