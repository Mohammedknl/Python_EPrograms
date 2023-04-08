students = [{'name': 'Alice', 'age': 20, 'grade': 95},{'name': 'Bob', 'age': 18, 'grade': 80},
            {'name': 'Charlie', 'age': 19, 'grade': 85},{'name': 'David', 'age': 21, 'grade': 90}]

# Sort the list of dictionaries by the 'grade' key in descending order
sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)

# Print the sorted list of dictionaries
for student in sorted_students:
    print(student)

