# https://www.youtube.com/@digitalrwanda

#lists

vegetables = ["apple", "banana", "cherry", "Mango"]

"""
[start:end]
0,1,2,----,10
"""

print(vegetables[::3])


#tuple

hummans = ('alice', "john", "emil", "grass")

print(hummans[:3])


string


h = "Hello, World!"

print(h[4::3])

#Camel case

    # def getUserData():
    #     return "user1"

    # getUserDatas = getUserData()

    # #PascarCase

    # class CustomerId:
    #     def __init__(self, id):
    #         return f"Id is returned automatically"

    # #snake_case

    # product_name = "I am Product Name"

    # #kebab-case

    # user-profile = "This is the kebab-case"


    # #SCREAMING_SNAKE_CASE

    # MAX_SPEED = 2910.32
    
    


# fruits = ["apple", "banana", "cherry"]

# fruits.append(("avocado","good"))
# fruits.extend(("Orange", "Berry"))

# fruits.insert(0, "Am first")

# fruits.remove("apple")

# fr = fruits.pop(-3)

# fruits.extend(fr)

# print(fruits.index("cherry"), " ", fruits[2])

# print(fruits)

# data = [1,2,3,4,5,True,False, 0, ""]

# out = [ i for i in data if i]

# print(any(data))


# x, y = map(int, input("Enter two numbers separated by space: ").split())

# import sys
# print("Argument received:", sys.argv[1], "name of scripts: ", sys.argv[0], "number of arguments: ", sys.argv)

# static_array = [None] * 5  # List with 5 elements, all set to None
# static_array[0] = 10
# static_array[1] = 20
# print(static_array)


# location: str = None

# lc_list: list[str] = ["home", "office", "gym"]

# while location not in lc_list:
#     location = input("Enter a location: ")

# print(location)

price = 4434088329.92039
widget = 9

msg = "The widget is {0:5} The price is {1:,.2f} \n"
msg1 = "The widget is {0:<05} < The price is {1:,.2f}"
msg2 = "The widget is {0:>05} > The price is {1:,.2f}"
msg3 = "The widget is {0:^06} == The price is {1:,.2f}"
# msg = "The widget is {w} The price is {p:,.2%}"

print(msg.format(widget,price))
print(msg1.format(widget,price))
print(msg2.format(widget,price))
print(msg3.format(widget,price))