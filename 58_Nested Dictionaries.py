# Subject : Nested Dictionaries in Python 
# Author : Muhammad Qamar
# Date : 2-August-2025
 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(f'{y} : {obj[y]}')
    print()



# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }



# thisdict = {
#     'child1' : {
#         'name' : "Ali"
#     },
#     'child2' : {
#         'name' : "Asad"
#     },
#     'child3' : {
#         'name' : "Muhammad"
#     },
#     'child4' : {
#         'name' : "Ahmed"
#     },
#     'child5' : {
#         'name' : "Qamar"
#     }
# }

# print(thisdict['child5']['name'])


