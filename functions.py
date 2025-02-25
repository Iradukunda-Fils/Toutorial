# https://www.youtube.com/@digitalrwanda


from typing import Union,Dict, Tuple, Callable, Any

def add(a: int, b: int) -> Union[int, float]:
    result = a + b
    return result

def swap(a: int, b:int, c: int) -> Tuple[int, int, int]:
    return c, b, a

print(swap(1,2,4))

def deposit(balance: Union[int, float], amount: Union[int, float]) -> Union[int, float]:
    return balance + amount
    
balance = 100

new_balance = deposit(balance, 5000)    

print(new_balance)


def process_transaction(balance: Union[int, float], type: str, amount: Union[int, float]) -> Union[int, float,str]:
    if amount <= 0:
        raise ValueError("The amount can't be zero..!")
    match type:
        case "deposit": 
            return balance + amount
        case "withdraw", if amount <= balance:
            return balance - amount
        case _: 
            return "Invalid type of transaction or amount provided not much with balance..!"

balance = 200

print(f"The original balance is: ", balance)

new_balance = process_transaction(balance,"deposit", 5000)

print(f"The new balance is: ", new_balance)

withdraw_balance = process_transaction(new_balance, "withdraw", 16000)

print("withdraw proceed and the balance is: ", withdraw_balance)



func = lambda x, y: f"{x} is greater" if x > y else f"{y} is greater"


print(func(10,5))

def greet(name: str, age: int,/, street: str,*, home: int = "Rwanda") -> Any:
    return "Welcome back {0} your age is: {1} location is at treet: {3} Home Country is: {2}".format(name,age,home,street)

var = greet("John Doe",30, street="KG15", home="USA")
var1 = greet("John Doe", 18)

print(var)
print(var1)


def add(*args:int, **kwargs: Dict[str,Any]) -> Any:
    print(type(args))
    print(type(kwargs))
    print(kwargs)
    print(kwargs.pop("name"))
    print(kwargs)
    return sum(args)

print(add(10,20, 30, name="John", age=30, street="KG15"))


def sum(n: int) -> int | float:
    if n == 0:
        return 0
    
    return n + sum(n-1)


# 0, 1, 2, 3
print(sum(3))








# import sys

# print(sys.getrecursionlimit())

# sys.setrecursionlimit(5000)

# print(sys.getrecursionlimit())




# def sum(n: int) -> int | float:
#     if n == 0:
#         return 0
#     a=n
#     return n + sum(a-1)

# print(sum(3))









    
    

    






