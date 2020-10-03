# https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN

year = int(input())
year = str(year)
y = year[0:2]
if int(year)/int(y) > 100:
    print(int(y) + 1)
else:
    print(int(y))
