#Write a function that counts vowels and consonants in a string.
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels =", vowels)
    print("Consonants =", consonants)

s = input("Enter a string: ")
count_vowels_consonants(s)