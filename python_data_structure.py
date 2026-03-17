# Lists
# It is ordered, mutable, allows duplicate elements, and is indexed.

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")    #add to end
fruits.remove("banana")   #remove item
fruits.insert(1, "grape")   #insert at index
fruits.pop()    #remove last item
fruits.sort()   #sort list
fruits.reverse()    #reverse list
print(fruits[0]) #access first item
print(fruits[1:3])   #access a range of items
print(len(fruits))   #length of list

# use lists for collections of items that may change, such as a list of tasks or a collection of user inputs.
#use lists when you need to perform operations that modify the collection, such as adding, removing, or sorting items.

#Tuples
# It is ordered, immutable, allows duplicate elements, and is indexed.
coordinates = (10, 20)
print(coordinates[0])   #access first item
print(coordinates[1])   #access second item

#use tuples for fixed collections of items, such as coordinates or RGB values.
# use tuples when you want to ensure that the data cannot be modified after creation, providing a level of data integrity.

# Dictionaries
# It is unordered (as of Python 3.7, it maintains insertion order), mutable, allows duplicate values but not duplicate keys, and is indexed by keys.
# It uses key-value pairs to store data.
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])   #access value by key
person["age"] = 31    #update value
person["country"] = "USA"   #add new key-value pair
del person["city"]    #remove key-value pair
print(person.keys())   #get all keys
print(person.values()) #get all values
#use dictionaries for collections of key-value pairs, such as a person's information or a mapping of items to their prices.
#use dictionaries when you need to access data by a unique key, allowing for efficient lookups and modifications based on those keys.
 
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 21, "grade": "A"}
}
print(students["Alice"]["grade"])   #access nested value


student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student["name"])   #access value by key
student["age"] = 21    #update value
student["country"] = "USA"   #add new key-value pair
del student["grade"]    #remove key-value pair

# loop through
for key, value in student.items():
    print(key, ":", value)


# Sets
# It is unordered, mutable, does not allow duplicate elements, and is not indexed.
unique_numbers = {1, 2, 3, 4, 4}
print(unique_numbers)   # Output: {1, 2, 3, 4}
unique_numbers.add(5)    #add element
unique_numbers.remove(2) #remove element
print(unique_numbers)   # Output: {1, 3, 4, 5}

#use sets for collections of unique items, such as a set of tags or a collection of unique user IDs.

#use sets when you need to perform operations that involve uniqueness, such as finding the intersection or union of two collections, or when you want to ensure that no duplicate items are stored.

# useful for comparision of two collections, such as finding common elements or unique elements between two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))   # Output: {3, 4}
print(a.union(b))          # Output: {1, 2, 3, 4, 5, 6}

# or

print(a & b)   # Output: {3, 4}
print(a | b)   # Output: {1, 2, 3, 4, 5, 6}


# Lists, tuples, dictionaries, and sets are fundamental data structures in Python that serve different purposes based on their characteristics. Understanding when to use each one is crucial for writing efficient and effective code.

# List 
for item in ["a", "b", "c"]:
    print(item)

# Tuple
for item in ("x", "y", "z"):
    print(item)

# Dictionary
for key, value in {"name": "Alice", "age": 30}.items():
    print(key, ":", value)

# Set
for item in {1, 2, 3}:
    print(item)

