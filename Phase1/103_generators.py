# You already know how lists hold all their elements in memory, right?
# Generators are different — they generate values on the fly, one at a time, when you need them.


# basic generator function
def square_list(n) -> list:
    return [x**2 for x in range(n)]

print(square_list(5))  # Output: [0, 1, 4, 9, 16]



# generator function using yield
def squares_gen(n):
    for x in range(n):
        yield x**2


gen = squares_gen(5)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4
print(next(gen))  # Output: 9
print(next(gen))  # Output: 16
# print(next(gen))  # Raises StopIteration      



for value in squares_gen(5):
    print(value)



# Generators are ideal when:
# You’re working with huge datasets (like reading millions of lines from a file).
# You only need one item at a time, not the whole list in memory.
# They’re lazy — they produce values only when needed, which saves both time and RAM.


# Memory Comparison
import sys

nums_list = [x for x in range(1_000_000)]
nums_gen = (x for x in range(1_000_000))

print(sys.getsizeof(nums_list))  # 8448728
print(sys.getsizeof(nums_gen))   # 200

