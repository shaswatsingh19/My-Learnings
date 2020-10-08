# Write a Python program to get the difference between the two lists.

lst1 = [2,4,5,11]
lst2 = [1,2,3,4]

# we are doing lst1-lst2
diff_lst1_lst2 = list(set(lst1)-set(lst2))

diff_lst2_lst1 = list(set(lst2)-set(lst1))

print(diff_lst1_lst2)
# output :- [11, 5]

print(diff_lst2_lst1)
# output :- [1, 3]