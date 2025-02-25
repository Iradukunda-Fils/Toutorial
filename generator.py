# https://www.youtube.com/@digitalrwanda

from typing import Generator,Union, Iterator

"""
Iterators

Generators
 
"""




# def generator():
#     value = yield "Generator started"
#     var = yield value 
#     yield var
#     return "generation Done"
    
# gen: Generator[int, str, str] = generator()


# try:
#     while True:
#         print(gen.send(None))
#         continue
# except StopIteration as e:
#     print(e.value)


# food = ["apple", "banana", "Cherry"]

# food: Iterator[int] = iter(food)

# print(next(food))
# print(next(food))
# print(next(food))
# print(next(food))

a = 10**2
print(a)
b = str(a)

print(len(b))

# def ranges(start: Union[int, float], stop: Union[int, float] = None, step: Union[int, float] = 1) -> Union[int, float]:
#     if stop is None:
#         stop = start
#         start = 0
#     if step == 0:
#         raise ValueError("The number of step can't be zero..!")
#     else:
#         while (step > 0 and start < stop) or (step < 0 and start > stop):
#             yield start
#             start += step
    
# # print(list(ranges(1,5,2)))

# for i in ranges(10):
#     print(i)