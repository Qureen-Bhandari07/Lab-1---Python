#WAP to reverse a string using for loop

string=input('Enter a string : ')
reverse=' '

for i in string:
    reverse=i+reverse
print('Reversed string : ',reverse)
