# Subject : Input in Python 
# Author : Muhammad qamar
# Date : 30th  August 2025

import math 

# print("Enter your name please : ")
# name = input()
# print(f"Hello! Welcome {name}")





# name = input("Enter your name please : ")
# print(f"Hello! Welcome {name}")






# name = input("Enter your name please : ")
# print(f"Hello! Welcome {name}")

# fav1 = input('Enter your favourite animal : ')
# fav2 = input('Enter your favourite color : ')
# fav3 = float(input('Enter your favourite number : '))

# print(f"Do you want {fav2} {fav1} with {fav3} legs ")












# x = input("Enter a number : ")

# y = math.sqrt(float(x))

# print(f"the square root of {x} is {y}")








while True:
    a = input("Enter a number : ")

    try :
        a = float(a)
        break 
    except ValueError:
        print("Invalid input please enter a number!")

b = math.sqrt(a)

print(f"the square root of {a} is {b} \n")
