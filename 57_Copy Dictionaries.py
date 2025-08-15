# Subject : Copy Dictionaries in Python 
# Author : Muhammad Qamar
# Date : 2-August-2025

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict1 = thisdict.copy()
# print(thisdict1)

thisdict1 = dict(thisdict)
print(thisdict1)

