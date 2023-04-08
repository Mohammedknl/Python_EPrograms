#Here we see the example on Division,Modulus and Flow division operators
'''Write a Program to convert given number of days to a measure of time given in years,weeks and days.
 For example 375 days is equal to 1 year 1 week and 3 days (ignore leap year )'''
days=int(input('Enter the No of days:\n'))
y=days//365 # Here we use  flow division operator as we require the quotient value always as int
rem=days%365 # Here we use Modulus operator as we require the remainder value
w=rem//7 # here we use Flow division operator again to obtain Quotient value
rd=rem%7 # Here we use modulus operator as we require remainder value
print('{} days has {} years,{} weeks and {} days'.format(days,y,w,rd))#as there are 4 place holders we have to define 4 values in .format method
