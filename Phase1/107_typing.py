# Type hints help both humans and tools (like VS Code or mypy) understand what’s supposed to go where.

def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Alice"))  # Output: Hello, Alice

# You’re not enforcing types — Python still runs dynamically — but you’re documenting intent.