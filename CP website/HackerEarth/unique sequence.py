s= input()
count = 1
for i in range(len(s)):
    if (s[i] != s[i+1]):
        count = count +1
print(count)
