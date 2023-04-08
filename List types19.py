# create a list of integers
my_list = [1, 2, 3, 4, 5]
# print the list
print("Original list:", my_list)
# append an element to the end of the list
my_list.append(6)
print("List after append:", my_list)
# insert an element at a specific index
my_list.insert(2, 7)
print("List after insert:", my_list)
# remove an element from the list
my_list.remove(3)
print("List after remove:", my_list)
# pop an element from the list
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after pop:", my_list)
# sort the list
my_list.sort()
print("List after sort:", my_list)
# reverse the list
my_list.reverse()
print("List after reverse:", my_list)
# get the index of an element
index = my_list.index(4)
print("Index of 4:", index)
# count the number of occurrences of an element
count = my_list.count(2)
print("Count of 2:", count)
# create a copy of the list
new_list = my_list.copy()
print("New list:", new_list)
# clear the list
my_list.clear()
print("List after clear:", my_list)
