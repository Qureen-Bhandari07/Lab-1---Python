#Write a function that calculates the sum of all numbers from 1 to n using a loop.
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter n: "))
print("Sum =", calculate_sum(n))