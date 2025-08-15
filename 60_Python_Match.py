# Subject : Python Match 
# Author : Muhammad Qamar
# Date : 15th- August - 2025


# day = 5

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")


# day = 4
# match day:
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Looking for weekend")


# day = 5
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Today is weekday!")
#     case 6 | 7:
#         print("Today is weekend!")


month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("Today is weekday of April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("Today is weekday of May")
    case _:
        print(" No Match!")