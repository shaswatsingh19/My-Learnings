def replace(s):
    ans= ''
    i=0
    while(i<len(s)-1):
        if(s[i]=='p' and s[i+1]=='i'):
            ans += '3.14'
            i+=2
        else:
            ans += s[i]
            i+=1
            
    if(i<len(s)):
        ans += s[i]
    return ans


s = 'pippppiiiipip'
print(replace(s))
