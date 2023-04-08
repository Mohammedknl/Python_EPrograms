try:
    a=int(input('ENter positive no:'))
    if a<0:
        raise ValueError('No negative numbers should endter from exception')
    else:
        print('Entered value of a is :',a)
except ValueError as e:
    print(e)

