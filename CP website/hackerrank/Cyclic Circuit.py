# https://www.hackerearth.com/challenges/competitive/april-circuits-20/algorithm/lets-shift-2-36d90caa/
def dec_bin(n):
    ans= ""
    while n!=0:
        rem = n%2
        ans = str(rem) + ans
        n = n// 2
    return ans

def conv_16bit(bit_8):
    bit = [0]*16
    ans = ""
    bit = bit[0:len(bit)-len(bit_8)]
    for i in bit:
        ans = ans + str(i)
    ans = ans + bit_8
    return ans

    
t = int(input())
while t:
    li = input().split()
    n=int(li[0])
    m=int(li[1])
    c=li[2]
    _8bit_bin = dec_bin(n)

    _16bit_bin = conv_16bit(_8bit_bin)
    d = ""
    if c == 'L':
         d = _16bit_bin[n:] + _16bit_bin[0:m]
    elif c =='R':
        d = _16bit_bin[len(_16bit_bin)-m:] + _16bit_bin[0:len(_16bit_bin)-m]

    d = int(d,2)
    print(d)
        
        
    t = t -1
