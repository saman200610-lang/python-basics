name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = (total / 300) * 100

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")