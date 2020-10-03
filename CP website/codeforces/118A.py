s = input()
for  i in range(len(s)):
    ch = s[i].lower()
    if (ch == 'a' or ch == 'i' or ch == 'o' or ch == 'e' or ch == 'u' or ch == 'y'):
        continue
    else:
        print("."+ch,end='')


