# Declare a string variable
my_string = "Hello World"
# Count the number of occurrences of a substring
count = my_string.count("l")
print("Number of 'l' in the string:", count)
# Find the index of a substring
index = my_string.find("World")
print("Index of 'World' in the string:", index)
# Check if the string only contains alphanumeric characters
is_alphanumeric = my_string.isalnum()
print("Is the string alphanumeric?", is_alphanumeric)
# Check if the string only contains alphabetic characters
is_alpha = my_string.isalpha()
print("Is the string alphabetic?", is_alpha)
# Check if the string only contains decimal characters
is_decimal = my_string.isdecimal()
print("Is the string decimal?", is_decimal)
# Check if the string only contains digits
is_digit = my_string.isdigit()
print("Is the string a digit?", is_digit)
# Check if the string is in lowercase or uppercase
is_lower = my_string.islower()
is_upper = my_string.isupper()
print("Is the string lowercase?", is_lower)
print("Is the string uppercase?", is_upper)

# Reverse the string
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)
