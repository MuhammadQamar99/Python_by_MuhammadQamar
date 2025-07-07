# Subject : Global Variables in Python
# Author : Muhammad Qamar
# Date : 7-July-2025

x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is",x)