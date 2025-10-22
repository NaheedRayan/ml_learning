

# The map function applies a given function to all items in an input list (or any iterable) and returns an iterator.
nums = [1, 2, 3, 4]
squares = map(lambda x: x**2, nums)
print(list(squares))  # [1, 4, 9, 16]
