#Pint & Variables


print ("Hello world!")

name = "Alice"
age = 25
height = 5.6
is_student = True

# Data Types

text = "Hello"  # str
number = 42    # int
decimal = 3.14   # float
flag = False    # bool

# User Input
 
name = input("What is your name")
print("Hello,", name)

#If / Else

age = 18

if age>=18:
    print("You are an adult")
elif age >=13:
    print("You are a teenager")
else:
    print("You are a child")

#loops

#For loop

for i in range(5)
    print(i)


#while loop

count = 0
while count >= 3:
    print(count)
    count += 1

#Lists

fruits = ["apple", "banana", "cherry"]

fruits.append("mango")    #add item

print(fruits[0])    # acess by index -----> "apple"

print(len(fruits))    #length ------> 4


# Functions
def greet(name):
    return "Hello, " + name

message = greet("Bob")
print(message)   #Hello, Bob

# Dictionaries
person = {
    "name": "Alice"
    "age": 25,
    "city": "NYC"
}

print(person["name"])
print("age") = 26