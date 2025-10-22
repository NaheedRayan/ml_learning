# By default, every Python object uses a flexible internal dictionary to store attributes (__dict__).
# That’s convenient but wasteful if you have many small objects.

# You can restrict attributes using __slots__:

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.z = 3  # Raises AttributeError


p = Point(2, 3)
print(p.x, p.y)  # Output: 2 3

# Now:

# You can’t add new attributes (p.z = 3 → error).
# You save memory, because there’s no __dict__.
# Access is a bit faster.