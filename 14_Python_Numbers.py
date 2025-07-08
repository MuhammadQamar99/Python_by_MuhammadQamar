# Subject : Numbers in Python
# Author : Muhammad Qamar
# Date : 08-July-2025

import random

x = 1    # int
y = 2.8  # float
z = 1j   # complex


# ==========================================

# Int Data-Type
a = 2345623456
b = -23456789987
c = 355723646141279812

print(type(a))
print(type(b))
print(type(c))

# ==========================================

# Float Data-Type
d = 234.5623456
e = -234567.89987
f = 3557236.46141279812

print(type(d))
print(type(e))
print(type(f))

g = 35e3
h = 12E4
i = -87.7e100

print(type(g))
print(type(h))
print(type(i))

# ==========================================

# Complex Data-Type
j = 5+3j
k = 6j
l = -7j

print(type(j))
print(type(k))
print(type(l))

# ==========================================

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = float(x)
y = int(y)
z = complex(x)
print(type(x))
print(type(y))
print(type(z))

# ==========================================

print(random.randrange(1,10))
