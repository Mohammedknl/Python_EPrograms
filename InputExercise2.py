'''
program that uses the input() function to ask the user for their name and age,
and then prints out a message welcoming them and telling them how many years
until they turn 100:
'''
# Ask the user for their name
name = input("What is your name? ")
# Ask the user for their age
age = int(input("What is your age? "))

# Calculate the number of years until the user turns 100
years_to_100 = 100 - age

# Print out a message using the comma operator
print("Hello", name + "!", "You are currently", age, "years old, and you will turn 100 in", years_to_100, "years.")
