# Subject : Polymorphism in Python 
# Author : Muhammad Qamar
# Date : 21th August 2025


# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model 
    
#     def move(self):
#         print("Drive!")


# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model 
    
#     def move(self):
#         print("Sail!")


# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model 
    
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford","Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for x in (car1,boat1,plane1):
#     x.move()









class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass
    # def __init__(self,brand,model):
    #     self.brand = brand
    #     self.model = model 
    
    # def move(self):
    #     print("Drive!")


class Boat(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
    
    def move(self):
        print("Fly!")

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1,boat1,plane1):
    x.move()