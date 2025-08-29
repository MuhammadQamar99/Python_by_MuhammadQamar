# Subject : Try and Except in Python 
# Author : Muhammad Qamar
# Date : 27th August 2025


# Exception Handling

# try:
#     print(x)
# except NameError:
#     print("Variable 'x' is not defined!")
# except:
#     print("Something went wrong")








# try:
#     print("hello")
# except:
#     print("something went wrong")
# else:
#     print("Nothing went wrong")






# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'Try-Except' has been completed")









# try:
#     f = open('demofie.txt')
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong when writing in the file.")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening in the file.")












age = int(input())
if age < 0:
    raise Exception("Sorry! Age can't be less than zero")
print(age)


