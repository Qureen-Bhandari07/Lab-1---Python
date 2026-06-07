#WAP that takes two numbers and performs : Addition, Subtraction, Multiplication, Division, Floor division, Modulus, Exponentiation

a , b= input('Enter value of a and b').split()

a=int(a)
b=int(b)

print('Add : ',a + b)
print('Subtract : ',a - b)
print('Multiply : ',a * b)
print('Divide : ',a /  b)
print('Floor division: ',a // b)
print('Modulus : ',a % b)
print("Exponentiation (power): ",a ** b)

