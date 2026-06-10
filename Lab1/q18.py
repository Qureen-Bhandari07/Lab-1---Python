# wap to check if the string is palindrome (reads the same froward and backward)

string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")