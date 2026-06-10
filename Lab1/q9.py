# wap that converts numerical marks to letter grades: 90-100 : A, 80-89:B, 70-19:C, 60-69:D, Below 60:F

marks = int(input("Enter your marks: "))

# Check grade using conditions
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks <= 89:
    print("Grade: B")
elif marks >= 70 and marks <= 79:
    print("Grade: C")
elif marks >= 60 and marks <= 69:
    print("Grade: D")
elif marks < 60 and marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks")