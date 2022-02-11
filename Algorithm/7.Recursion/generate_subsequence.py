a = [3,1,2]
n = 3
# subsequence = 2^n
def f(i,l):
    if i>=n:
        print(l)
        return 
    l.append(a[i])
    f(i+1,l) # add and pass to function
    l.remove(a[i])
    f(i+1,l) # remove and pass to function
    
    

f(0,[])