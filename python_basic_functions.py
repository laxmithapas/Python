#  Basic Function
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!


# Functions with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!

# Function with Return Value
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

# Function with Default Parameters
def greet(name, message="Good morning"):
    print(f"{message}, {name}!")

greet("Alice")                    # Good morning, Alice!
greet("Bob", "Good evening")      # Good evening, Bob!

# FUCNTION WITH MULTIPLIE RETURN VALUES
def get_info():
    name = "Alice"
    age = 25
    return name, age          # returns a tuple

name, age = get_info()
print(name, age)    # Alice 25

# *args — Multiple Arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))         # 6
print(add_all(10, 20, 30, 40))  # 100

# *ARGGS - LET YOU PASS ANY  NUMBER OF ARGUMENTS TO A FUNCTION
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25, city="New York")

# LAMBDA FUNCTION
square = lambda x: x * x
print(square(5))  # Output: 25

# RECURSIVE FUNCTION
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# **kwargs — Keyword Arguments
def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC

# Scope — Where Variables Live

x = 10    # Global variable — available everywhere

def my_function():
    y = 20    # Local variable — only inside function
    print(x)  # ✅ can access global
    print(y)  # ✅ can access local

my_function()
print(x)    # ✅ works
# print(y)  ❌ ERROR — y doesn't exist outside!

#  Global Keyword

count = 0    # global

def increment():
    global count     # tell Python to use the global one
    count += 1

increment()
increment()
print(count)    # 2





