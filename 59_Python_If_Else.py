# Subject : Python If ... Else
# Author : Muhammad Qamar
# Date : 14-August-2025


# Python If ... Else
a = 33
b = 54

if a > b:
    print("yes b is greater than a")

if b > a:
    print("B is greater than a")



a = 33
b = 33

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equals to b")



a = 31
b = 33

if a > b:
    print('yes a is greater than b')
elif a == b:
    print('a is equals to b')
else:
    print('a is less than b')



a = 33
b = 43

# if a < b : print("a is less than b")

print('a is greater than b') if a > b else print("a is less than b")

a = 330
b = 330

print('a') if a > b else print("=") if a == b else print("b")






a = 20
b = 30
c = 50

# if a < b and b < c:   # and , or operators are oppsoite of each other ( OKAY )
#     print("Yes")


# if a < b or b > c:
#     print("Yes a < b")

# if not a > b:
#     print("Yes")


x = 40

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("No x is not greater  than 20")