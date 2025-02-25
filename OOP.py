# https://www.youtube.com/@digitalrwanda



class Person: 
    blood_group = "O"
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    
    def dancing(self, name: str) -> str:
        return f"I know how to dance, and I am {name}"
    
    def running(self) -> str:
        return "I know how to run"
    
    def sleep_in_class(self) -> str:
        return "I know outcome of sleeping in the class"
    
    def blood(self, group: str) -> str:
        b=self.blood_group
        self.blood_group = group
        return f"The bood group is changed from {b} to {self.blood_group}"
        

person1 = Person("Ketia", 18, "Female")


print(person1.blood("AA"))

print(person1.name)
print(person1.age)
print(person1.gender)
print(person1.blood_group)


person2 = Person("John Doe", 45, "Male")

print("\n")

print(person2.blood("AB"))

print(person2.name)
print(person2.age)
print(person2.gender)
print(person2.blood_group)


from typing import Union

class Math:
    def __init__(self, a: Union[int, float], b: Union[int, float]) -> None:
        self.num1: Union[int, float] = a
        self.num2: Union[int, float] = b
        
    def multiply(self)-> int | float:
        result = self.num1 * self.num2
        return f"The product is {result}"
    
    def division(self)-> int | float:
        result = self.num1 / self.num2
        return f"The division output is {result}"
    
    def fool_division(self)-> int | float:
        result = self.num1 // self.num2
        return f"The fool division output is {result}"
    def modulus(self)-> int | float:
        result = self.num1 % self.num2
        return f"The fool division output is {result}"
    
    def add(self)-> int | float:
        result = self.num1 + self.num2 
        return f"The addition is: {result}"
    
    def subtraction(self) -> int | float:
        result = self.num1 - self.num2
        return f"The subtraction output is {result}"
    
    
# obj1: Math = Math(9,2)


# print(obj1.add(6))


class Quadratic(Math, Person):
    def add(self) -> int | float:
        self.num1 = 15
        return super().add()



print(Quadratic.mro())

"""
MRO: Method Resolution Older


C3 linearization: 


"""



quadr: Math = Quadratic(10,15)

print(quadr.add())






"""
Python Order of Operations

PEMDAS:

P: Parentheses () : highest precedence

E: Exponents ** 

MD: Multiplication and Division *, /, //, %

AS: Addition and Subtraction +, -

Comparison: <, >, <=, >=

Logical: not, and, or

"""


print(6+4-2*4-6/5)

# 6+4-8

    

def ranges(start: int, stop: int = None, step: int = 1) -> int:
    if stop is None:
        stop = start
        start = 0
        
    if step == 0:
        raise ValueError("Yield got unexpected output..?")
        
    while (step > 0 and  start < stop) or (step < 0 and start > stop):
        yield start
        start += step
        
print(x for x in ranges(1,4))


print(range(4))

for i in ranges(1,5,2):
    print (i)

    
