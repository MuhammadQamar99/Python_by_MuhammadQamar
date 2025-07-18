# Subject : Copy Lists in python
# Author : Muhammad Qamar
# Date : 18-July-2025


# list1 = ['apple','banana','orange']
# list2 = list1
# list1.append('cherry')
# print(list2)


# # Use the copy() method
# this_list = ['apple','banana','orange']
# new_list = this_list.copy()

# this_list.append('cherry')
# print(new_list)


# Use the slice Operator
this_list1 = ['apple','banana','orange']
new_list2 = this_list1[:]

this_list1.append('cherry')
print(new_list2)