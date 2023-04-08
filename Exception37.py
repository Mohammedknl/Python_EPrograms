a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
try:
    c=a/b
    print('Division=',c)
except ZeroDivisionError as e:
    print(e)
print('Will this line print?')