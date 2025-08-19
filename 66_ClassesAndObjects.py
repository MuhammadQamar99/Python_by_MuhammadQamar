# Subject : Classes and Objects in Python 
# Author : Muhammad Qamar
# Date : 18th August 2025



# # Example
# class Myclass:
#     x = 5
# o = Myclass()
# print(o.x)






# # Create a class named Person, use the __init__() method to assign values for name and age:
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Muhammad",17)

# print(p1.name)
# print(p1.age)





# # The string representation of an object WITHOUT the __str__() method:
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p2 = Person("Muhammad",17)
# print(p2)






# # The string representation of an object WITH the __str__() method:
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} ({self.age})"

# p3 = Person("Muhammad",17)
# print(p3)





# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")

p4 = Person("Muhammad",17)

p4.age = 40
p4.myfunc()
