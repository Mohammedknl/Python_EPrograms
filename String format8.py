'''Prog:Write a program to accept two values from user,
find addition and print the result'''
a=int(input('Enter a value:\n'))
b=int(input('Enter b value:\n'))
c=a+b
# I way
print('Addition of',a,'and',b,'is',c)
#II way
print('Addition of %d and %d is %d'%(a,b,c))# Using Format specifier but it is depricated means there is better solution than this and not recommended to use
#III Way
print('Addition of {} and {} is {}'.format(a,b,c))