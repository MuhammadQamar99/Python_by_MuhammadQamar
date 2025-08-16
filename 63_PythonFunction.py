# Subject : Functions in Python  
# Author : Muhammad Qamar
# Date : 16th August 2025



# Example of Function
# def my_function():
#     print("Hello, World!")
#     print("Subscribe to my Channel")

# my_function()





# def say_name(fname):
#     print("Muhammad " + fname )

# say_name("Ali")
# say_name("Omar")
# say_name("omair")






# def full_name(fname,lname):
#     print(fname + " " + lname)

# full_name("Muhammd","Qamar")






# def myfuntion(*kids):
#     print("The youngest child is " + kids[-1])

# myfuntion('Taimoor','Sameer','Muhammad','Abubakar')




# def thisfunction(child1,child2,child3):
#     print("The youngest child is " + child3)

# thisfunction(child3='Ali',child2='Omar',child1='haris')




# def this_function(**kids):
#     print('The youngest child is ' + kids['y'])

# this_function(a="Ali",b='harry',y='Omar')



# def countryfinder(country = "Pakistan"):
#     print("I am from " + country)

# countryfinder("Norway")
# countryfinder("Newzealand")
# countryfinder('Iran')
# countryfinder()



# def the_function(food):
#     for i in food:
#         print(i)


# fruits = ['apple','banana','cherry','orange','mango']
# the_function(fruits)




# def thefunction(x):
#     return 10 * x

# print(thefunction(5))




def tri_recurse(k):
    if (k > 0):
        result = k + tri_recurse(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Result: ")
tri_recurse(6)