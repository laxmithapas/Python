# Create strinngs

single = 'Hello'
double = "World"
multi = """hello,
how are you?
I am fine."""


name = "Alice"
print("len(name)")   # Output: 5
print(name[0])   # Output: 'A'
print(name[1:4])   # Output: 'lic'
print(name.upper())   # Output: 'ALICE'
print(name.lower())   # Output: 'alice'
print(name.replace("Alice", "Bob"))   # Output: 'Bob'
print(name.split("i"))   # Output: ['Al', 'ce']
print("Hello, " + name)   # Output: 'Hello, Alice'
print(f"Hello, {name}")   # Output: 'Hello, Alice'
print(name.isalpha())   # Output: True
print(name.isdigit())   # Output: False
print(name.startswith("A"))   # Output: True
print(name.endswith("e"))   # Output: True
print(name.strip())   # Output: 'Alice' (removes leading and trailing whitespace)
print(name[-1])   # Output: 'e' (access last character)


# use strings for text data, such as names, messages, or any sequence of characters.
# use strings when you need to perform operations that involve text manipulation, such as formatting, searching, or replacing parts of the text.




# Slicing strings
text = "Hello, World!"
print(text[0:5])   # Output: 'Hello'
print(text[7:])    # Output: 'World!'
print(text[:5])    # Output: 'Hello'
print(text[-6:])   # Output: 'World!'

text[start : stop : step]
text = "Hello, World!"
print(text[0:5:2])   # Output: 'Hlo'
print(text[::2])     # Output: 'Hlo ol!'
# By setting the step to 2, you tell Python to take every second character. It starts at 'H', skips 'e', takes 'l', skips 'l', takes 'o', and so on.
print(text[::3])   # Output: 'Hl r!'
# By setting the step to 3, you tell Python to take every third character. It starts at 'H', skips 'e' and 'l', takes 'l', skips 'o' and ',', takes ' ', and so on.

print(text[::-1])  # Output: '!dlroW ,olleH'
# By setting the step to -1, you tell Python to reverse the string. It starts at the end of the string and takes characters in reverse order until it reaches the beginning.

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.split())   # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# By default, the split() method splits the string at whitespace characters (spaces, tabs,

sentenche = "   hello, world!   "
print(sentence.strip())   # Output: 'hello, world!' (removes leading and trailing whitespace)
# The strip() method removes any leading and trailing whitespace characters from the string. In this case
print(sentence.replace("hello ", "hi"))   # Output: '   hi, world!   ' (replaces 'hello ' with 'hi')
# The replace() method replaces all occurrences of the specified substring with another substring. In this case
print(sentence.split(", "))   # Output: ['   hello', 'world!   '] (splits the string at ', ')
# The split() method splits the string at the specified separator. In this case, it splits
print("python" in sentence)   # Output: False (checks if 'python' is in the sentence)
print(sentence.count("o"))   # Output: 2 (counts the number of occurrences of 'o' in the sentence)

# string formatting
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))   # Output: 'My name is Alice and I am 30 years old.'
# The %s is a placeholder for a string, and %d is a placeholder for an integer. The values of name and age are inserted into the string in the order they are provided in the tuple.
print("My name is {} and I am {} years old.".format(name, age))   # Output: 'My name is Alice and I am 30 years old.'
# The {} are placeholders for the values that will be inserted. The format() method takes the values as arguments and replaces the placeholders in the string with those values in the order they are provided.
print(f"My name is {name} and I am {age} years old.")   #   Output: 'My name is Alice and I am 30 years old.'
# The f-string allows you to embed expressions inside string literals, using curly braces {}. The values of name and age are directly inserted into the string where the placeholders are located, making it a more concise and readable way to format strings compared to the older % formatting or the str.format() method.


# usefull string checks
print("Hello".isalpha())   # Output: True (checks if all characters are alphabetic)
print("123".isdigit())   # Output: True (checks if all characters are digits)
print("Hello, World!".startswith("Hello"))   # Output: True (checks if the string starts with 'Hello')
print("Hello, World!".endswith("!"))   # Output: True (checks if the string ends with '!')

#Joining and splitting strings

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.split())   # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# The split() method splits the string into a list of substrings based on the specified separator
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(" ".join(words))   # Output: 'The quick brown fox jumps over the lazy
# The join() method takes an iterable (in this case, a list of words) and concatenates its elements into a single string, with the specified separator (in this case, a space) between each element.
print("-".join(words))   # Output: 'The-quick-brown-fox-jumps-over-the-lazy-dog'
# By using a different separator (in this case, a hyphen), you can join the
