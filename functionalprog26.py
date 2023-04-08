def func():
    return 'Hello'
# This defines a function named "func" that returns the string "Hello" when called.
x = func()
# Here, we call the function "func()" and store the returned string "Hello" in the variable "x".
print(type(x))
# This prints the type of the value stored in x, which is a string.
y = func
# Here, we assign the function "func" to the variable "y". Notice that we don't call the function.
print(x)
# This prints the value stored in x, which is the string "Hello".
print(y)
# This prints the memory address of the function object that "y" refers to.
print(y())
# This calls the function object that "y" refers to, which returns the string "Hello" and prints it.
print(type(y))
# This prints the type of the object that "y" refers to, which is a function.
print(type(x))
# This prints the type of the object that "x" refers to, which is a string.
