# write a program to count the number of vowels in a string
text=input("Enter a string: ")
count = 0

'''for ch in text:
    if ch in 'aeiouAEIOU':
        count = count+1

print('Number of vowels : ',count)
'''
string = input("Enter a string: ")

count = 0
i = 0

while i < len(string):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u' or string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
        count = count + 1
    i = i + 1

print("Number of vowels =", count)