# Declare a string variable
my_string = "The quick brown fox jumps over the lazy dog"

# Get the length of the string
length = len(my_string)
print("Length of the string:", length)

# Convert the string to uppercase
uppercase_string = my_string.upper()
print("Uppercase string:", uppercase_string)

# Remove whitespace from the beginning and end of the string
trimmed_string = my_string.strip()
print("Trimmed string:", trimmed_string)

# Split the string into a list of words
words = my_string.split()
print("Words in the string:", words)

# Replace a substring in the string
new_string = my_string.replace("fox", "cat")
print("New string:", new_string)

# Check if the string starts with a prefix
starts_with = my_string.startswith("The")
print("Starts with 'The'?", starts_with)

# Check if the string ends with a suffix
ends_with = my_string.endswith("dog")
print("Ends with 'dog'?", ends_with)
