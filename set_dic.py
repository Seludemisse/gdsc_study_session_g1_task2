'''Task: Student Database

Create a simple student database program using Python dictionaries and basic data types. The program should be able to perform the following actions:

Add Student: Allow the user to add a new student to the database. Collect information such as name, age, grade, and any other relevant details.

View Student: Allow the user to view the details of a specific student by entering the student's name.

List All Students: Display a list of all students in the database with their basic information.

Update Student Information: Allow the user to update the information of a specific student, such as changing their grade or age.

Delete Student: Allow the user to delete a student from the database based on their name.

'''
students = {}

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    sex = input("Enter student sex: ")
    dept = input("Enter student dept: ")
    grade = input("Enter student grade: ")
  
    
    students[name] = {
        'age': age,
        'sex' : sex,
        'dept':dept,
        'grade': grade
      
    }
    
    print("Student added successfully.")

def view_student():
    name = input("Enter student name: ")
    
    if name in students:
        student = students[name]
        print("Name:", name)
        print("Age:", student['age'])
        print("Sex:", student['sex'])
        print("Dept:", student['dept'])
        print("Grade:", student['grade'])
     
    else:
        print("Student not found.")

def list_all_students():
    if students:
        print("List of students:")
        for name, student in students.items():
            print("Name:", name)
            print("Age:", student['age'])
            print("Sex:", student['sex'])
            print("Dept:", student['dept'])
            print("Grade:", student['grade'])
            
    else:
        print("No students found.")

def update_student():
    name = input("Enter student name: ")
    
    if name in students:
        student = students[name]
        age = input("Enter new age (press enter to keep current age): ")
        sex = input("Enter new age (press enter to keep current sex): ")
        dept = input("Enter new age (press enter to keep current age): ")
        grade = input("Enter new grade (press enter to keep current grade): ")
       
    
        
        if age:
            student['age'] = age
        if grade:
            student['grade'] = grade
        
        print("Student information updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name: ")
    
    if name in students:
        del students[name]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nStudent Info")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            list_all_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


    main()