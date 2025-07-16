# Subject : List Comprehension in python 
# Author : Muhammad Qamar
# Date : 16-July-2025


# # List Comprehension
# mylist = ['mango','apple','banana','cherry','orange','kiwi']
# newlist = []

# for x in mylist:
#     if 'a' not in x:
#         newlist.append(x)

# print(newlist)


# # using list comprihension
# mylist = ['mango','apple','banana','cherry','orange','kiwi']
# newlist = [i for i in mylist if 'a' not in i]
# print(newlist)

# newlist1 = [x for x in mylist if  x != 'apple']
# print(newlist1)


# mylist = ['mango','apple','banana','cherry','orange','kiwi']
# newlist = [x for x in mylist]
# print(newlist)


# thislist = [ x for x in range(10)  ]
# print(thislist)


# thislist = [ x for x in range(10) if x < 5 ]
# print(thislist)


# thislist = [ x for x in range(10) if x % 2 == 0 ]
# print(thislist)


# thislist = [ x for x in range(10) if x % 2 != 0 ]
# print(thislist)

# mylist = ['mango','apple','banana','cherry','orange','kiwi']
# newlist = [x.upper() for x in mylist]
# print(newlist)

# newlist1 = [x.title() for x in newlist]
# print(newlist1)


mylist = ['mango','apple','banana','cherry','orange','kiwi']
newlist = [x if x != 'banana' else 'orange' for x in mylist]
print(newlist)