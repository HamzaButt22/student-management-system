student_database = []

def Store_Records(name, student_id, gpa):
    store_records = {
        "Name": name,
        "ID": student_id,
        "GPA": gpa
    }
    student_database.append(store_records)
    print(f"✔️ Record for {name} saved successfully!")

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
    if not student_database:
        print("\nNo student records found in the database.")
        return
    else:
        print("\n=========================")
        print("  STUDENT RECORD SYSTEM  ")
        print("=========================")
        for student in student_database:
            print("Name:", student["Name"])
            print("ID:", student["ID"])
            print("GPA:", student["GPA"])
            print("-------------------------")

def Input():
    name = input("Enter student name: ")
    if validate_Name(name) == True:
        student_id = input("Enter student ID: ")
        if validate_Student_ID(student_id) == True:
            duplicate_found = False
            for student in student_database:
                if student["ID"] == int(student_id):
                    print("Error: A student with this ID already exists.")
                    duplicate_found = True
                    break
            if duplicate_found:
                return 

            gpa = input("Enter student GPA: ")
            if validate_GPA(gpa) == True:
                Store_Records(name, int(student_id), float(gpa))

def Search_Student_Record():
    if not student_database:
        print("\nThe database is completely empty. Add students first.")
        return

    search_id = input("Enter student ID to search: ")
    if validate_Student_ID(search_id) == True:
        found = False
        for student in student_database:
            if student["ID"] == int(search_id):
                print("\n🔍 Student Record Found:")
                print("Name:", student["Name"])
                print("ID:", student["ID"])
                print("GPA:", student["GPA"])
                print("-------------------------")
                found = True
                break
        if not found:
            print("No record found for Student ID:", search_id)

def Menu():  
    while True:
        print("\nWelcome to the Student Record System!")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student Record")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            Input()
        elif choice == "2":
            Display_All_Records()
        elif choice == "3":
            Search_Student_Record()
        elif choice == "4":
            print("\nExiting the Student Record System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

Menu()