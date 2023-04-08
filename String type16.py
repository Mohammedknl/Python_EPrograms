# Creating a string
my_string = "Hello, world!"
# Accessing a character by index
print(my_string[0]) # Output: 'H'
# Slicing a string
print(my_string[0:5]) # Output: 'Hello'
# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name
print(message) # Output: 'Hello, Alice'
# Formatting strings
age = 30
message = "I am {} years old".format(age)
print(message) # Output: 'I am 30 years old'
# Converting case
print(my_string.upper()) # Output: 'HELLO, WORLD!'
print(my_string.lower()) # Output: 'hello, world!'
# Searching for a substring
if "dorld" in my_string:
    print("Found 'world'") # Output: 'Found 'world''
else:
    print('Word not found')
