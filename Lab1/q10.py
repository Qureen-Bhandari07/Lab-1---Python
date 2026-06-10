# WAP that takes three numbers and finds the largest among them using if-elif-else

num1,num2,num3 = input("Enter three numbers : ") .split()

#convert the input number into the int
num1=int(num1)
num2=int(num2)
num3=int(num3)

if num1>num2 and num1>num3:
    print(num1,"is greatest.")
elif num2>1 and num2>num3:
    print(num2,'is greatest.')
else:
    print(num3,"is greatest.")