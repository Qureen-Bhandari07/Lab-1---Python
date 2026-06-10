# wap to check if a person is eligible to vote. Also check if they are senior citizen (age>=60)
age=int(input('Enter your age: '))
if age<18:
    print("NOT ELIGIBLE TO VOTE!")
print("To check age")
if age>50:
    print("SENIOR CITIZEN DETECTED.")
else:
    print('Not a senior citizen.')