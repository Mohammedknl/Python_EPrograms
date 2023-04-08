# Initialize the sum variable
total = 0
# Use a for loop to iterate over the numbers from 0 to 10
for i in range(11):
    # Check if the number is even
    if i % 2 == 0:
        # If it is, add it to the total
        total += i
# Print the sum of all even numbers
print("The sum of all even numbers between 0 and 10 is:", total)
