# other codes

#If conditions

# price = int(input("Enter The price: "))

# if 30 <= price and price <= 50:
#     print("The price is: {:.2f}".format(price) , "The price is in range!")
# elif price %2 == 0:
#     print("The number is even number")
#     if price == 12 or price == 10:
#         print("the price is equal to 12 or 10")
        
#     elif price == 8:
#         print("the value is 8")
#     else: 
#         print("Done")
        
# elif price == 3:
#     print("The value is 3")
# else:
#     print("The price is not in range! and is odd")

# For loop

# range(start, end, step)

# for i in range(1, 10+1,3):
#     if i == 4:
#         print("The 4 is in range")
#         continue
#     print("i is: %d " % i)

# food = ('apple', 'banana', "cherry", "Avocado")

# dic = {
#     "name":"John Doe",
#     "age": 32,
#     "Degree": "phd",
#     "Country": "Rwanda"
# }

# for k, v in dic.items():
#     print(f"This {k} is: {v}")



# food = (['apple','red_apple', 'blue_apple',"red_apple"], ['banana', 'red_banana', "blue_banana"], ["cherry", "red_cherry", "blue_cherry"], ["Avocado", "red_avocado", "Blue_avocado"])

# for num in range(1, 11):
#     for i in range(1,11):
#         print(f"{num} * {i} = {num*i}")
#     print("\n")
    
# for i in food:
#     print(i)
#     for item in i:
#         print(item)


# for i in range(1, 10+1):
#     print(i)
    
    
# for i in range(10):
#     print(i)

# var = ['food', "potatoes", "avocado", "orange", "egg"]
# guess = 0
# a = input("Enter element: ")
# while a not in var:
#     guess += 1
#     if guess == 3:
#         print("you tried too long..!")
#         break
#     else:
#         a = input("Try again but 3 times: ")
#         if a in var:
#             print("Print the element {} is in list..!".format(a))
#             break
#         continue

# print("the event successful..!")

# user = {
#     "username": "fils",
#     "password": 1234
# }


# var = ['banana', "apple", "cherry", "avocado"]

# food = input("enter food to test: ")

# try_time = 1
# while food not in var:
#     if try_time < 1:
#         print("You try too long")
#         break
#     elif try_time <= 5:
#         print("The food not found")
#         food = input("Try again: ")
#     else:
#         break
#     try_time += 1
    

# print("Done food is correct..!")

# user = {
#     "username": "Fils",
#     "password": "1234"
# }

# a =  input("enter username: ")
# b = input("enter password: ")

# guess = 0
# while a != user["username"] and b != user["password"]:
#     guess += 1
#     if guess <= 3:
#        print("incorrect credentials..!")
#        a = input("ty again with your username: ")
#        b = input("password: ")
#        continue
#     else:
#         print("to many try..!")
#         break
   
# print("Operation pass..!")


# import random

# while True:
#     real = random.randint(1,10)
#     user = int(input("Try to enter any number for guess for 1 - 10: "))
    
#     if real == user:
#         print("You have passed the game..!")
#         break
#     else:
#         print("Game Over you loose..! The real is: {}".format(real))
#         continue


