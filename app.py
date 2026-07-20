class Student:
    student_database = []

    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def Display_All_Records(self):
        if not Student.student_database:
            print("\nNo student records found in the database.")
            return
        else:
            print("\n=========================")
            print("  STUDENT RECORD SYSTEM  ")
            print("=========================")
            for student in Student.student_database:
                print("Name:", student.name)
                print("ID:", student.student_id)
                print("GPA:", student.gpa)
                print("-------------------------")    

    def Update_gpa(self, new_gpa):
        if validate_GPA(new_gpa) == True:
            self.gpa = float(new_gpa)
            print(f"✔️ GPA for {self.name} updated successfully to {self.gpa}!")
        else:
            print("Error: Invalid GPA format. Update failed.")

def Store_Records(name, student_id, gpa):
    new_student = Student(name, student_id, gpa)
    Student.student_database.append(new_student)
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

def Input():
    name = input("Enter student name: ")
    if validate_Name(name) == True:
        student_id = input("Enter student ID: ")
        if validate_Student_ID(student_id) == True:
            duplicate_found = False
            for student in Student.student_database:
                if student.student_id == int(student_id):
                    print("Error: A student with this ID already exists.")
                    duplicate_found = True
                    break
            if duplicate_found:
                return

            gpa = input("Enter student GPA: ")
            if validate_GPA(gpa) == True:
                try:
                    final_id = int(student_id)
                    final_gpa = float(gpa)
                    Store_Records(name, final_id, final_gpa)
                except ValueError:
                    print("Error: Invalid GPA format.")
                    return

def Search_Student_Record():
    if not Student.student_database:
        print("\nThe database is completely empty. Add students first.")
        return

    search_id = input("Enter student ID to search: ")
    if validate_Student_ID(search_id) == True:
        found = False
        for student in Student.student_database:
            if student.student_id == int(search_id):
                print("\n🔍 Student Record Found:")
                print("Name:", student.name)
                print("ID:", student.student_id)
                print("GPA:", student.gpa)
                print("-------------------------")
                found = True
                break
        if not found:
            print("No record found for Student ID:", search_id)

def Update_Student_Record():
    if not Student.student_database:
        print("\nThe database is empty. No records to update.")
        return

    update_id = input("Enter student ID to update GPA: ")
    if validate_Student_ID(update_id) == True:
        found = False
        for student in Student.student_database:
            if student.student_id == int(update_id):
                new_gpa = input(f"Enter new GPA for {student.name}: ")
                student.Update_gpa(new_gpa)
                found = True
                break
        if not found:
            print("No record found for Student ID:", update_id)

def Menu():  
    while True:
        print("\nWelcome to the Student Record System!")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student Record")
        print("4. Update Student GPA")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            Input()
        elif choice == "2":
            Student.Display_All_Records(Student)
        elif choice == "3":
            Search_Student_Record()
        elif choice == "4":
            Update_Student_Record()
        elif choice == "5":
            print("\nExiting the Student Record System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

Menu()