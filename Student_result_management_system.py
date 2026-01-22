
# Student Result Management System

print("STUDENT RESULT MANAGEMENT SYSTEM")

# Input student details
student_name = input("Enter student name: ")

score1 = int(input("Enter score for Subject 1: "))
score2 = int(input("Enter score for Subject 2: "))
score3 = int(input("Enter score for Subject 3: "))

# Processing
total_score = score1 + score2 + score3
average_score = total_score / 3

# Grade and remark
if average_score >= 70:
    grade = "A"
    remark = "Excellent"
elif average_score >= 60:
    grade = "B"
    remark = "Very Good"
elif average_score >= 50:
    grade = "C"
    remark = "Good"
elif average_score >= 45:
    grade = "D"
    remark = "Fair"
else:
    grade = "F"
    remark = "Fail"

# Output
print("\n--- STUDENT RESULT ---")
print("Student Name:", student_name)
print("Total Score:", total_score)
print("Average Score:", average_score)
print("Grade:", grade)
print("Remark:", remark)
