class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return "Invalid arguments"
    def subtract(self, *args):
        if len(args) == 2:
            return args[0] - args[1]
        elif len(args) == 3:
            return args[0] - args[1] - args[2]
        else:
            return "Invalid arguments"
calculator = Calculator()
print(calculator.add(1, 2))  # prints 3
print(calculator.add(1, 2, 3))  # prints 6
print(calculator.add(1, 2, 3, 4))  # prints "Invalid arguments"
print(calculator.subtract(10, 2))  # prints 8
print(calculator.subtract(10, 2, 1))  # prints 7
print(calculator.subtract(10, 2, 1, 5))  # prints "Invalid arguments"
'''
In this example, we define a Calculator class with an add and a subtract method, both of which accept variable-length arguments using *args. 
In the add method, we check the length of the args tuple and return the appropriate sum. Similarly, in the subtract method, we check the length of the args tuple and return the appropriate difference.
If the length of the args tuple is not 2 or 3, we return an error message.

We can then create an instance of the Calculator class and call the add and subtract methods with different numbers of arguments.
The appropriate method is called based on the number of arguments provided.

'''