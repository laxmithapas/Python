# 1 Simple Print Python

print("Hello, World")

# 2 Importing Modules

import math
import os
import random

   # or importing specific function

from math import sqrt
from datetime import datetime

# 3 Defining fucntions first

def greet(name)
    print(f"Hello, {name}!")
greet("Alice")

# 4 The if__name__ == "__main__" Block

def main():
    print("Programm starts here")
if __name__ == "__main__":
    main()

# 5 Variables and Constant at the top
Name = "Alice"
Age = 25
PI =  3.14159
print(NAME, AGE)

# 6 Class defination

# For object oriented programming

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Rex") 
my_dog.bark()
