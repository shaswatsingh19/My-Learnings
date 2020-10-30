def remove_0_4_5(li):
    li.pop(0)
    li.pop(3)
    li.pop(3)
    return li




li =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print('Before Removing')
print(li)
print('After Removing')
print(remove_0_4_5(li))
