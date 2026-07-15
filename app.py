student_database = []

def Store_Records(name, student_id, gpa):
    store_records = {
        "Name": name,
        "ID": student_id,
        "GPA": gpa
    }
    student_database.append(store_records)

def Display_All_Records():
    print("\nStudent Record System!\n")
    for student in student_database:
        print("Name:", student["Name"])
        print("ID:", student["ID"])
        print("GPA:", student["GPA"])
        print("-------------------------\n")

Store_Records("John Doe", 12345, 3.5)
Store_Records("Jane Smith", 67890, 3.8)

Display_All_Records()