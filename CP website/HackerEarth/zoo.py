xcount = 0
ycount= 0
str = input()
print(str)
print(list(str))
for i  in list(str):
    if(i == 'z'):
        xcount = xcount +1
    if(i == 'o'):
        ycount = ycount + 1
if(ycount == 2*xcount):
    print("Yes")
