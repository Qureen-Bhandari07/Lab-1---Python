#Write a function that takes a number and returns whether it's even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))