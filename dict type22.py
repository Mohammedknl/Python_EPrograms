person = {'name': 'John', 'age': 25, 'favorite_food': 'pizza'}
print("My name is " + person['name'])
print("I am " + str(person['age']) + " years old")
print("My favorite food is " + person['favorite_food'])
person['age'] = 26
person['favorite_food'] = 'sushi'
print("My updated age is " + str(person['age']))
print("My new favorite food is " + person['favorite_food'])
for key, value in person.items():
    print(key + ": " + str(value))
