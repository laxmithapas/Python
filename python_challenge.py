# 1. Ask user for their full name
# 2. Print it in UPPERCASE
# 3. Count how many characters it has
# 4. Check if their name starts with "A"

name = input("Enter your name:")
print(f"Uppercase: {name.upper()}")
print(f"length of the charcters: {len(name)}")
print(f"the name starts with A: {name.startswith('A')}")