# a = int(input("Enter a temperature in celsius:"))

# b = (a * 9/5) + 32

# print(f"The temperature in Fehrenhite: {b}")

# a = int(input("Enter the number:"))

# if a % 2 == 0:
#     print(f"{a} is even!")
# elif a % 2 != 0:
#     print(f"{a} is odd!")
# else:
#     print("You Entered Zero")


# a = int(input("Enter the number:"))
# if a % 2 == 0:
#     print("You have Enterd Zero")
# elif a % 3 == 0:
#     print("Fizz")
# elif a % 5 == 0:
#     print("Buzz")
# elif a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz")
# else:
#     print(a)

# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = input("Enter the operator(+,-,*,/):")
# if c == "+": 
#     print(f"The addition of {a} and {b} is: {int(a) + int(b)}")
# elif c == "-": 
#     print(f"The subtraction of {a} and {b} is: {int(a) - int(b)}")
# elif c == "*": 
#     print(f"The multiplication of {a} and {b} is: {int(a) * int(b)}")
# elif c == "/": 
#     print(f"The division of {a} and {b} is: {int(a) / int(b)}")
# else: 
#     print("Invalid operator!")

# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the third number:"))

# if a > b and b > c:
#     print(f"{a} is the greatest number")
# elif b > a and b > c:
#     print(f"{b} is the greatest number")
# elif c > a and c > b:
#     print(f"{c} is the greatest number")

a = int(input("Enter the first number:"))
for i in range (1, 11):
    i = i * a
    print(i)
    