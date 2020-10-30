# Write a Python program to remove duplicates from a list.

a = [11,22,43,14,43]
di = {}
for i in a:
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1
for k,v in di.items():
    if v==2:
        print(k)