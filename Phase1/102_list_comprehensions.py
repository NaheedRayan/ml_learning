

# A comprehension is a shorter, cleaner way to create a new list, set, or dictionary from 
# something you’re looping over — often replacing several lines of code with one.


# Normal way
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Using List Comprehension
squares_comp = [x**2 for x in range(10)]
print(squares_comp)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# General Syntax:
# new_list = [expression for item in iterable if condition]

# Example with condition
evens = [x for x in range(10) if x%2 ==0]
print(evens)  # Output: [0, 2, 4, 6, 8]


# Example: Create a list of squares of even numbers from 0 to 9
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # Output: [0, 4, 16, 36, 64]


# list of all odd numbers between 1 and 20, but instead of the numbers themselves, you store the string "odd" repeated that many times?
# (e.g. for 3 → "oddoddodd")
ans = [x*"odd" for x in range(1,21) if x%2 !=0]
print(ans)  # Output: ['odd', 'oddodd', 'oddoddodd', 'oddoddoddodd', 'oddoddoddoddodd', 'oddoddoddoddoddodd', 'oddoddoddoddoddoddodd', 'oddoddoddoddoddoddoddodd']