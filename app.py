student_database = []

def Store_Records(name, student_id, gpa):
    store_records = {
        "Name": name,
        "ID": student_id,
        "GPA": gpa
    }
    student_database.append(store_records)

    
def validate_Name(name):
    if name == "":
        print("Error: Name is required.")
        return False
    if len(name) < 3 or len(name) > 50:
        print("Error: Name must be between 3 and 50 characters.")
        return False
    if name.replace(" ", "").isalpha() == False:
        print("Error: Name must contain only letters and spaces.")
        return False
    return True

def validate_Student_ID(student_id):
    if student_id == "":
        print("Error: Student ID is required.")
        return False
    if not student_id.isdigit():
        print("Error: Student ID must be a number.")
        return False
    if len(student_id) != 5:
        print("Error: Student ID must be exactly 5 digits.")
        return False
    return True
    
def validate_GPA(gpa):
    if gpa == "":
        print("Error: GPA is required.")
        return False
    if "-" in gpa:
        if gpa.count("-") > 1 or not gpa.startswith("-"):
            print("Error: GPA must be a valid number format.")
            return False
    if gpa.lstrip("-").startswith("."):
        print("Error: Please include a leading zero (e.g., 0.5 or -0.5 instead of .5 or -.5).")
        return False
    if gpa.count(".") > 1:
        print("Error: GPA cannot contain multiple decimal points.")
        return False
    if not gpa.lstrip("-").replace(".", "", 1).isdigit():
        print("Error: GPA must be a number.")
        return False
    if "." in gpa:
        if len(gpa.split(".")[1]) > 2:
            print("Error: GPA cannot have more than 2 decimal places.")
            return False
    if float(gpa) < 0.0 or float(gpa) > 4.0:
        print("Error: GPA must be between 0.0 and 4.0.")
        return False
    return True

def Display_All_Records():
    print("\nStudent Record System!\n")
    for student in student_database:
        print("Name:", student["Name"])
        print("ID:", student["ID"])
        print("GPA:", student["GPA"])
        print("-------------------------\n")

name = input("Enter student name: ")

if validate_Name(name) == True:
    student_id = input("Enter student ID: ")
    if validate_Student_ID(student_id) == True:    
        gpa = input("Enter student GPA: ")
        if validate_GPA(gpa) == True:
            Store_Records(name, int(student_id), float(gpa))
            Display_All_Records()