NAME:Akinsola Oluwsemilore Inioluwa

MATRIC NO: 24/14063

DEPARTMENT: Computer Science


1. Requirement Analysis (Student Result System)

Functional Requirements

The Student Result System shall:
	•	Accept student_name
	•	Accept subject1_score
	•	Accept subject2_score
	•	Accept subject3_score
	•	Calculate total_score
	•	Calculate average_score
	•	Display grade
	•	Display remark

Non-Functional Requirements
	•	The Student Result System shall be easy to use
	•	The Student Result System shall run on Python
	•	The Student Result System shall give accurate results

2. System Design

Input Design
	•	student_name
	•	subject1_score
	•	subject2_score
	•	subject3_score

Process Design
	•	Calculate total_score
	•	Calculate average_score
	•	Determine grade
	•	Determine remark

Output Design
	•	total_score
	•	average_score
	•	grade
	•	remark

  

3. Implementation

Programming Language: Python
File Name: main.py
Repository Name: student-result-system

4.
# Student Result System

print("STUDENT RESULT SYSTEM")

student_name = input("Enter student name: ")

subject1_score = int(input("Enter subject 1 score: "))
subject2_score = int(input("Enter subject 2 score: "))
subject3_score = int(input("Enter subject 3 score: "))

total_score = subject1_score + subject2_score + subject3_score
average_score = total_score / 3

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

print("\n--- STUDENT RESULT ---")
print("Student Name:", student_name)
print("Total Score:", total_score)
print("Average Score:", average_score)
print("Grade:", grade)
print("Remark:", remark)

5. Testing

The Student Result System was tested using different score values to ensure correct calculation of:
	•	total_score
	•	average_score
	•	grade
	•	remark



6. Deployment

The system was deployed by uploading the files to GitHub.


7. Maintenance

Future improvements may include:
	•	Adding more subjects
	•	Saving results to a file

