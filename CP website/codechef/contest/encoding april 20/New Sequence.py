# https://www.codechef.com/ENCD2020/problems/ECAPR203

t = int(input())
li = []
while t:
    n = int(input())
    li.append(n)
    t = t -1

max_li = max(li)
seq = []
i =0
temp = max_li
while temp>0:
    i= i +1
    for k in range(i+1):
        seq.append(k)
        temp = temp -1
for i in li:
    print(seq[i-1])
