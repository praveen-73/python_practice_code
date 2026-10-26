# # inpu='tommorrow'

# # count=0
# # values=[]
# # for i in inpu:
# #     if i=='o':
# #         count=count+1
# #         i=count* '*'
# #         values.append(i)
# #     else:
# #         values.append(i)
# # print("".join(values))

# # for i in range(len(values)):
# #     for j in range(1+i,len(values)):
# #         if values[i]>values[j]:
# #             tem=values[i]
# #             values[i]=values[j]
# #             values[j]=tem

# # print("".join(values))
# my_set ='aabbccdd'

# values=[]
# for i in my_set:
#     if i not in values:
#       count=0
#       for j in my_set:
#          if i==j:
#             count+=1
            
        
#       print(f"{i}{count}",end="")
#       values.append(i)

    






students = []


def add_student():
    name = input("enter student name or exit: ").strip()

    if name.lower() == "exit":
        print("Adding student cancelled.")
        return

    while name == "":
        print("Name cannot be empty!")
        name = input("enter student name or exit: ").strip()

        if name.lower() == "exit":
            print("Adding student cancelled.")
            return

    while True:
        try:
            id = int(input("enter your id: "))

            if id < 0:
                print("ID cannot be negative!")
            elif any(student["id"] == id for student in students):
                print("This ID already exists!")
            else:
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    while True:
        try:
            age = int(input("enter your age: "))

            if age >= 0:
                break
            else:
                print("Age cannot be negative!")

        except ValueError:
            print("Invalid input! Please enter a number.")

    grades = {}

    for i in range(1, 4):
        key = input(f"Enter subject {i}: ").strip()

        while key == "" or key in grades:
            if key == "":
                print("Subject name cannot be empty!")
            else:
                print("This subject already exists!")

            key = input(f"Enter subject {i}: ").strip()

        while True:
            try:
                value = int(input(f"Enter grade in subject {key}: "))

                if 0 <= value <= 100:
                    break
                else:
                    print("Invalid grade! Enter a grade between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

        grades[key] = value

    student = {
        "name": name,
        "id": id,
        "age": age,
        "grades": grades
    }

    students.append(student)
    print("add_student is done.")


def view_all_students():
    if len(students) == 0:
        print("no student found.")
    else:
        for student in students:
            print(f"name: {student['name']}")
            print(f"id: {student['id']}")
            print(f"age: {student['age']}")

            if len(student["grades"]) > 0:
                print("Grades:")
                for subject in student["grades"]:
                    print(f"{subject}: {student['grades'][subject]}")
            else:
                print("No grades available.")

            print("-" * 20)


def search_student():
    while True:
        try:
            test = int(input("enter id to search a student: "))

            if test >= 0:
                break
            else:
                print("ID cannot be negative!")

        except ValueError:
            print("Invalid input! Please enter a number.")

    found = False

    for student in students:
        if test == student["id"]:
            print("This student exists.")
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Age: {student['age']}")

            for subject in student["grades"]:
                print(f"{subject}: {student['grades'][subject]}")

            found = True
            break

    if found == False:
        print("this student does not exist.")


def update_grades():
    while True:
        try:
            test = int(input("enter id to update: "))

            if test >= 0:
                break
            else:
                print("ID cannot be negative!")

        except ValueError:
            print("Invalid input! Please enter a number.")

    found = False

    for student in students:
        if test == student["id"]:
            found = True

            print("Available subjects:")

            for subject in student["grades"]:
                print(subject)

            subject = input("Enter subject name: ").strip()

            if subject in student["grades"]:
                while True:
                    try:
                        new_grade = int(input("enter your new grade: "))

                        if 0 <= new_grade <= 100:
                            break
                        else:
                            print(
                                "Invalid grade! Enter a grade between 0 and 100."
                            )

                    except ValueError:
                        print("Invalid input! Please enter a number.")

                student["grades"][subject] = new_grade
                print("Grade updated successfully.")

            else:
                print("subject not found.")

            break

    if not found:
        print("this student not found!")


def calculate_avrege():
    if len(students) == 0:
        print("no student found.")
        return

    for student in students:
        if len(student["grades"]) > 0:
            average = sum(student["grades"].values()) / len(student["grades"])

            if average >= 90:
                print(
                    f"{student['name']}: grades average -> {average:.2f} "
                    "& final result: excellent."
                )
            elif average >= 80:
                print(
                    f"{student['name']}: grades average -> {average:.2f} "
                    "& final result: Very Good."
                )
            elif average >= 70:
                print(
                    f"{student['name']}: grades average -> {average:.2f} "
                    "& final result: Good."
                )
            elif average >= 50:
                print(
                    f"{student['name']}: grades average -> {average:.2f} "
                    "& final result: pass."
                )
            else:
                print(
                    f"{student['name']}: grades average -> {average:.2f} "
                    "& final result: fail."
                )
        else:
            print("this student has no grades!")


def show_top_student():
    top = -1
    top_student = None

    for student in students:
        if len(student["grades"]) > 0:
            average = sum(student["grades"].values()) / len(student["grades"])

            if average > top:
                top = average
                top_student = student

    if top_student is not None:
        print(f"the Top Student: {top_student['name']}")
        print(f"Average: {top:.2f}")

        for student in students:
            if student != top_student and len(student["grades"]) > 0:
                average = sum(student["grades"].values()) / len(student["grades"])

                if average == top:
                    print(f"the Top Student: {student['name']}")
    else:
        print("No students with grades found!")


def delete_student():
    while True:
        try:
            test = int(input("enter id to search a student: "))

            if test >= 0:
                break
            else:
                print("ID cannot be negative!")

        except ValueError:
            print("Invalid input! Please enter a number.")

    found = False

    for student in students:
        if test == student["id"]:
            students.remove(student)
            found = True
            print("Student deleted successfully.")
            break

    if not found:
        print("student not found.")


def show_statistics():
    print("Total students:", len(students))

    total_grades = 0
    count = 0
    highest_average = None
    lowest_average = None
    passing_students = 0
    failing_students = 0

    for student in students:
        if len(student["grades"]) > 0:
            average = sum(student["grades"].values()) / len(student["grades"])

            print(f"{student['name']}: grades average -> {average:.2f}")

            if highest_average is None or average > highest_average:
                highest_average = average

            if lowest_average is None or average < lowest_average:
                lowest_average = average

            if average >= 50:
                passing_students += 1
            else:
                failing_students += 1

            for grade in student["grades"].values():
                total_grades += grade
                count += 1

        else:
            print(f"{student['name']}: No grades available")

    if count > 0:
        overall_average = total_grades / count

        print("Class average:", round(overall_average, 2))
        print("Highest average:", round(highest_average, 2))
        print("Lowest average:", round(lowest_average, 2))
        print("Passing students:", passing_students)
        print("Failing students:", failing_students)
    else:
        print("No grades available.")


while True:
    print("""STUDENT MANAGEMENT SYSTEM
1. Add a New Student
2. View All Students
3. Search for a Student
4. Update Student Grades
5. Calculate Student Average
6. Show the Top Student
7. Delete a Student
8. Show Statistics
9. Exit""")

    while True:
        try:
            choice = int(input("Choose a number at the menu: "))

            if 1 <= choice <= 9:
                break
            else:
                print("Invalid menu option! Choose from 1 to 9.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    if choice == 1:
        add_student()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_grades()
    elif choice == 5:
        calculate_avrege()
    elif choice == 6:
        show_top_student()
    elif choice == 7:
        delete_student()
    elif choice == 8:
        show_statistics()
    elif choice == 9:
        print("Goodbye!")
        break