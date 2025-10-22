


# normal class
class Point:
    def __init__(self , x:int, y:int):
        self.x = x
        self.y = y

# But dataclasses let Python auto-generate that __init__, plus __repr__, __eq__, etc., for you:

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(2, 3)
p2 = Point(2, 3)

print(p1)          # Output: Point(x=2, y=3)
print(p1 == p2)   # Output: True

# So — it’s like a shortcut for simple data containers.
