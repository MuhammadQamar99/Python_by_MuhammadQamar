# Subject : Inheritance in Python 
# Author : Muhammad qamar
# Date : 19th August 2025


# class Father:     # Base Class
#     pass

# class Child(Father):      # Derived Class
#     pass 






# # Create a Parent Class
# class Person:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def print_name(self):
#         print(f'{self.first_name} {self.last_name}')

# p1 = Person("Muhammad",'Qamar')
# p1.print_name()


# class Student(Person):
#     pass

# p2 = Student("John",'Doe')
# p2.print_name()











# # Create a Parent Class
# class Person:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def print_name(self):
#         print(f'{self.first_name} {self.last_name}')

# p1 = Person("Muhammad",'Qamar')
# p1.print_name()


# class Student(Person):
#     def __init__(self, first_name, last_name,year):
#         super().__init__(first_name,last_name )
#         self.year = year

#     def welcome(self):
#         print(f"Welcome {self.first_name} {self.last_name} to the class of {self.year}")

# p2 = Student("John",'Doe',2019)
# p2.welcome()