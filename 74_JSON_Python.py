# Subject : JSON in Python 
# Author : Muhammad Qamar
# Date : 24th August 2025


import json 

# # Some JSON
# x = '{"name" : "Muhammad", "age" : 17, "city": "Islamabad"}'
# print(x)

# # Parse Json
# y = json.loads(x)

# print(y['age'])
# print(y)







# a = {
#     'name' : 'Qamar',
#     'age' : 20,
#     'city' : 'Islamabad'
# }


# b = json.dumps(a)
# print(b)








c = {
    'name' : 'Ali',
    'age' : 54,
    'married' : True,
    'divorced' : False,
    'pets' : None,
    'cars' : [
        {'model' : 'BMW', "mpg": 27.5}
    ]
}

print(json.dumps(c, indent=2, separators=('. ','= '), sort_keys=True))