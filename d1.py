# program to find missing
A = [4,6,3,2,7,8,9]
missing = [i for i in range(10) if i not in A]
print('missing numbers are: ', missing)

# reverse the string as 
# "I am boy" -> "I ma yob"
original = "I am boy"
reverse = ''
for word in original.split(' '):
    reverse += word[::-1] + ' '
print('reverse string : ',reverse)