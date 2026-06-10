def reverse_string(text):
    reverse = ""

    for i in text:
        reverse = i + reverse

    return reverse

s = input("Enter a string: ")
print("Reversed String =", reverse_string(s))