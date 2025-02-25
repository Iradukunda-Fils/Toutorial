# https://www.youtube.com/@digitalrwanda


class P:
    def __repr__(self):
        return "Dealing..!"
    
food = ["apple", "banana", "cherry"]

try:
    a = int(input("Enter age: "))
    
    # if a:
    #     raise TypeError("This is type error..!")
    
    if a > 18:
        print("you are older enough..!")
    else:
        print("too young..!")

except ZeroDivisionError as e:
    print("Zero Division error..!", e)
    
except TypeError as e:
    print("This is Type error: ", e)

except Exception as e:
    print("sorry exception meet! and is: ", e)

else:
    print("the action successful completed..!")

finally:
    print("The codes is executed..!")
