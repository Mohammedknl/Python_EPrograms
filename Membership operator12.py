# Membserhip operator will check wether the particular element is available in the string/sequence or not we can check string/list/tuple
ch=input('Enter any character:')
#print("It is Vowel") if ch in 'a,e,i,o,u' else print('It is Consonents') # This is with Membership operator in
#print("It is Vowel") if not(ch in 'a,e,i,o,u') else print('It is Consonents') # This is with Logical not operator
print("It is a consonent") if ch not in 'a,e,i,o,u' else print('It is vowel') # This is with Membership operator not in