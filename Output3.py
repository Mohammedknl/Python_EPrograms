# Output a string
print("hello, world")

# Output a variable
x = 42
print(x)

# Output multiple objects
name = "Alice"
age = 30
print(name, "is", age, "years old")

# Specify a custom separator
print("hello", "world", sep="...")

# Specify a custom end string
print("hello", end="")
print("world")

# Write output to a file
with open("output.txt", "w") as f:
    print("hello, file", file=f)
