# Subject : Loop Dictionaries in Python 
# Author : Muhammad qamar
# Date : 2-August-2025


this_dict = {
    'name' : 'muhammad',
    'age' : 17,
    'year' : 2025
}

# for x in this_dict:
#     print(x)

# for x in this_dict:
#     print(this_dict[x])

# for i in this_dict:
#     print(f"{i} : {this_dict[i]}")

for x,y in this_dict.items():
    print(x,":",y)