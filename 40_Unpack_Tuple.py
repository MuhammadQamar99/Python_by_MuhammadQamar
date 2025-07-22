# Subject : Unpack Tuples in python 
# Author : Muhammad qamar
# Date : 22-July-2025



# # Unpacking a Tuple
# fruits = ("apple", "banana", "cherry")
# (a,b,c) = fruits
# print(a)
# print(b)
# print(c)


# fruits = ("apple", "banana", "cherry", "kiwi", "mango", 'orange')
# (a,b,*c) = fruits
# print(a)
# print(b)
# print(c)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)