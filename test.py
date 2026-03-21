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


a = int(input("Enter the number:"))
if a % 2 == 0:
    print("You have Enterd Zero")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
else:
    print(a)