# Subject : Scope in Python 
# Author : Muhammad Qamar
# Date : 22th August 2025


# # Local Scope

# def myfunc():
#     x = 26
#     print(x)

# myfunc()



# def myfunc2():
#     x = 20

#     def myfunc3():
#         print(x)
#     myfunc3()

# myfunc2()





# # Global Scope
# x = 10

# def myfunc4():
#     print(x)

# myfunc4()

# print(x)






# # Naming Variable
# x = 300

# def myfunc5():
#     x = 200
#     print(x)

# myfunc5()

# print(x)



# # Global Keyword
# def myfunction():
#     global x
#     x = 35
#     print(x)

# myfunction()


# print(x)




# x = 40
# def myfunction2():
#     global x
#     x = 45
#     print(x)

# myfunction2()
# print(x)






def newfunc():
    x = 23

    def newfunc2():
        nonlocal x 
        x = 15
    newfunc2()

    return x

print(newfunc())