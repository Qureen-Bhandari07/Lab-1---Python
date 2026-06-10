#Create a function that converts marks to grades using if-elif-else.
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = int(input("Enter marks: "))
print("Grade:", grade(marks))