# Write a Python program to print the numbers of a specified list after removing even numbers from it

def remove_even(li):
    i = 0
    while i < len(li):
        if li[i]%2 ==0:
            li.pop(i)
            i -=1
        i+=1
    return li
lst = [5,11,44,20,55,100,111]
print('List now:',lst)
print('After removing even number',remove_even(lst))