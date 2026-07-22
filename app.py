import numpy as np
import json

class Student:
    student_database = []

    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def display(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("GPA:", self.gpa)

    def Display_All_Records(self):
        if not Student.student_database:
            print("\nNo student records found in the database.")
            return
        else:
            print("\n=========================")
            print("  STUDENT RECORD SYSTEM  ")
            print("=========================")
            for student in Student.student_database:
                student.display()
                print("-------------------------")
                    

    def Update_gpa(self, new_gpa):
        if validate_GPA(new_gpa) == True:
            self.gpa = float(new_gpa)
            print(f"✔️ GPA for {self.name} updated successfully to {self.gpa}!")
        else:
            print("Error: Invalid GPA format. Update failed.")


class GraduateStudent(Student):
    def __init__(self, name, student_id, gpa, thesis_topic):
        super().__init__(name, student_id, gpa)
        self.thesis_topic = thesis_topic

    def display(self):
        super().display()
        print("Thesis Topic:", self.thesis_topic)


def Store_Records(name, student_id, gpa, thesis_topic=None):
    if thesis_topic:
        new_student = GraduateStudent(name, student_id, gpa, thesis_topic)
    else:
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

def Input(is_grad):
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
                    if is_grad == "y":
                        thesis_topic = input("Enter thesis topic: ")
                        Store_Records(name, final_id, final_gpa, thesis_topic)
                    else:
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
                student.display()
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

def Save_To_JSON():
    json_data = []
    for student in Student.student_database:
        record = {
            "name": student.name,
            "student_id": student.student_id,
            "gpa": student.gpa
            }
        if hasattr(student, 'thesis_topic'):
            record["thesis_topic"] = student.thesis_topic
        json_data.append(record)
    with open("students.json", "w") as file:
        json.dump(json_data, file, indent=4)

def Load_From_JSON():
    try:
        with open("students.json", "r") as file:
            loaded_data = json.load(file)
            for data in loaded_data:
                if "thesis_topic" in data:
                    new_student = GraduateStudent(data["name"], data["student_id"], data["gpa"], data["thesis_topic"])
                else:
                    new_student = Student(data["name"], data["student_id"], data["gpa"])
                Student.student_database.append(new_student)
    except FileNotFoundError:
        pass

def Calculate_Class_Statistics():
    if Student.student_database == []:
        print("\nThe database is empty. No records to calculate statistics.")
        return
    else:
        gpas = [student.gpa for student in Student.student_database]
        n = len(gpas)

        total_sum = 0.0
        for gpa in gpas:
            total_sum += gpa
        manual_mean = total_sum / n

        manual_max = gpas[0]
        manual_min = gpas[0]
        for gpa in gpas:
            if gpa > manual_max:
                manual_max = gpa
            if gpa < manual_min:
                manual_min = gpa

        sorted_gpas = sorted(gpas)
        if n % 2 != 0:
            manual_median = sorted_gpas[n // 2]
        else:
            mid1 = sorted_gpas[n // 2 - 1]
            mid2 = sorted_gpas[n // 2]
            manual_median = (mid1 + mid2) / 2

        squared_diff_sum = 0.0
        for gpa in gpas:
            squared_diff_sum += (gpa - manual_mean) ** 2
        manual_variance = squared_diff_sum / n
        manual_std_dev = manual_variance ** 0.5

        frequency = {}
        for gpa in gpas:
            if gpa in frequency:
                frequency[gpa] += 1
            else:
                frequency[gpa] = 1

        manual_mode = gpas[0]
        max_count = 0
        for gpa, count in frequency.items():
            if count > max_count:
                max_count = count
                manual_mode = gpa

        numpy_mean = np.mean(gpas)
        numpy_median = np.median(gpas)
        numpy_max = np.max(gpas)
        numpy_min = np.min(gpas)
        numpy_std_dev = np.std(gpas)
        
        values, counts = np.unique(gpas, return_counts=True)
        max_index = np.argmax(counts)
        numpy_mode = values[max_index]

        print("\n=============================================")
        print("  DESCRIPTIVE STATISTICS VERIFICATION SCREEN ")
        print("=============================================")
        print(f"Metric             | Manual Loop | NumPy Vector")
        print("---------------------------------------------")
        print(f"Average GPA        |    {manual_mean:.2f}     |    {numpy_mean:.2f}")
        print(f"Median GPA         |    {manual_median:.2f}     |    {numpy_median:.2f}")
        print(f"Mode GPA           |    {manual_mode:.2f}     |    {numpy_mode:.2f}")
        print(f"Highest GPA        |    {manual_max:.2f}     |    {numpy_max:.2f}")
        print(f"Lowest GPA         |    {manual_min:.2f}     |    {numpy_min:.2f}")
        print(f"Standard Deviation |    {manual_std_dev:.2f}     |    {numpy_std_dev:.2f}")
        print("=============================================")


def Menu():  
    while True:
        print("\nWelcome to the Student Record System!")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student Record")
        print("4. Update Student GPA")
        print("5. View Class Statistics")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            is_grad = input("Is this a Graduate Student? (y/n): ").strip().lower()
            Input(is_grad)
        elif choice == "2":
            Student.Display_All_Records(Student)
        elif choice == "3":
            Search_Student_Record()
        elif choice == "4":
            Update_Student_Record()
        elif choice == "5":
            Calculate_Class_Statistics()
        elif choice == "6":
            Save_To_JSON()
            print("\nExiting the Student Record System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

Load_From_JSON()
Menu()