# Get user's score
score = int(input("Enter your score (0-100): "))

# Check grade using conditional statements
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print result
print(f"Your grade is: {grade}")