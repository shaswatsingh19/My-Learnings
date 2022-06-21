def str_to_int(s):
    if len(s)==1:
        return ord(s[0])-ord('0')

    val = str_to_int(s[1:])

    ans = ord(s[0]) - ord('0')

    ans = ans*(pow(10,len(s)-1))+ val


    return ans

