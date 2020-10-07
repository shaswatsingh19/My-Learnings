# Write a Python function that takes two lists and returns True if they have at least one common member.


def oneCommon(l1,l2):
    for i in range(len(l1)):
        if l1[i] in l2:
            return True
        return False





l1 = [3,6,2,5,0]
l2 = [6,2,4]

if oneCommon(l1,l2):
    print('YES')
else:
    print('NO')
