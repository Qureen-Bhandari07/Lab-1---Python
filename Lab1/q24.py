#Write functions to find maximum and minimum in a list without using built-in max()/min().
def find_max(lst):
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum

def find_min(lst):
    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    return minimum

numbers = [10, 25, 3, 50, 18]

print("Maximum =", find_max(numbers))
print("Minimum =", find_min(numbers))