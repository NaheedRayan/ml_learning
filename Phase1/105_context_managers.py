# Step 1: What problem do context managers solve?
f = open("data.txt", "r")
data = f.read()
f.close()


# If something goes wrong (say, an error occurs while reading), f.close() might never run, 
# leaving the file open — that can cause memory leaks or file locks.
# So, Python gave us a cleaner, safer way to automatically manage setup and cleanup 
# actions → that’s what context managers do.


with open("data.txt" , "r") as f:
    data = f.read()
# Here, f is automatically closed when the block is exited, even if an error occurs.



# Lets make our own context manager using a class
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return "Some Resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True  # Suppress exception if any
    

with MyContext() as resource:
    print(resource)
    # raise ValueError("Oops!")  # Try uncommenting this

# When an error happens inside the with block, Python still calls the __exit__() method — 
# that’s the whole point of context managers: cleanup always happens.