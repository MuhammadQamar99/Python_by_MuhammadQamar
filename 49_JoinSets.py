# Subject : Join Sets in Python
# Author : Muhammad Qamar
# Date : 28-July-2025


# union() Method
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# this_set = set1.union(set2)
# print(this_set)

# this_set2 = set1 | set2 
# print(this_set2)


# # Multiple Sets Join
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# this_set3 = set1.union(set2,set3,set4)
# print(this_set3)

# this_set4 = set1 | set2 | set3 | set4
# print(this_set4)

# # Mutiple data-types
# set5 = {1,2,3}
# mytuple = ('a','b','c')

# this_set5 = set5.union(mytuple)
# print(this_set5)

# # Update() method
# set6 = {"a", "b" , "c"}
# set7 = {1, 2, 3}

# set6.update(set7)
# print(set6)


# intersection() method
# set8 = {"apple", "banana", "cherry"}
# set9 = {"google", "microsoft", "apple"}

# this_set6 = set8.intersection(set9)
# print(this_set6)

# this_set7 = set8 & set9
# print(this_set7)

# # intersection_update() method
# set10 = {"apple", "banana", "cherry"}
# set11 = {"google", "microsoft", "apple"}

# set10.intersection_update(set11)
# print(set10)


# set12 = {"apple", 1,  "banana", 0, "cherry"}
# set13 = {False, "google", 1, "apple", 2, True}

# set12.intersection_update(set13)
# print(set12)


# # difference() method
# set14 = {"apple", "banana", "cherry"}
# set15 = {"google", "microsoft", "apple"}

# this_set9 = set14.difference(set15)
# print(this_set9)

# this_set10 = set14 - set15
# print(this_set10)


# symmetric_difference() method
set16 = {"apple", "banana", "cherry"}
set17 = {"google", "microsoft", "apple"}

# this_set11 = set16.symmetric_difference(set17)
# print(this_set11)

this_set12 = set16 ^ set17
print(this_set12)