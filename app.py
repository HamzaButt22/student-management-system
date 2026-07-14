def student(name, student_id, gpa):
    print("\nStudent Record System!")
    print("Name:", name)
    print("ID:", student_id)
    print("GPA:", gpa)

name = input("Enter Student Name: ")

student_id = int(input("Enter Student ID: "))

gpa = float(input("Enter Student GPA: "))

student(name, student_id, gpa)
