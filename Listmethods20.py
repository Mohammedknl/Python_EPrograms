my_list = [1, 2, 3, 4, 5]

# append an element
my_list.append(6)
print(my_list)  # prints [1, 2, 3, 4, 5, 6]

# insert an element
my_list.insert(2, 7)
print(my_list)  # prints [1, 2, 7, 3, 4, 5, 6]

# extend the list
my_list.extend([8, 9])
print(my_list)  # prints [1, 2, 7, 3, 4, 5, 6, 8, 9]

# remove an element
my_list.remove(3)
print(my_list)  # prints [1, 2, 7, 4, 5, 6, 8, 9]

# pop an element
popped = my_list.pop()
print(popped)   # prints 9
print(my_list)  # prints [1, 2, 7, 4, 5, 6, 8]

# get index of an element
index = my_list.index(4)
print(index)    # prints 3

# count occurrences of an element
count = my_list.count(7)
print(count)    # prints 1

# sort the list
my_list.sort()
print(my_list)  # prints [1, 2, 4, 6, 7, 8]

# reverse the list
my_list.reverse()
print(my_list)  # prints [8, 7, 6, 4, 2, 1]

# clear the list
my_list.clear()
print(my_list)  # prints []
