x=[(22,1),(33,2),(11,4)]
x.sort()
print('This is without passging function as argument:',x)
y=[(22,1),(33,2),(11,4)]
def fun(y):
    return y[1]
y.sort(key=fun)
print('This is sorting list of tuple with second parameter by passign func as key:',y)
r=[2,-1,0.3,4]
def area(x):
    return 2.14*x*x
a=list(map(area,r))
print('This is by passing func area as argument to another func:',a)