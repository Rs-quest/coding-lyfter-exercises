from student import Student
import sys

def student_exists(student_list, full_name, student_class):
    for student in student_list:
        if (
            student.name.lower() == full_name.lower()
            and student.section.lower() == student_class.lower()
        ):
            return True

    return False

def is_valid_section(student_class):
    return (
        len(student_class) == 3
        and student_class[:2].isdigit()
        and student_class[2].isalpha()
    )

def is_valid_name(full_name):
    return full_name.strip() != "" and not any(
        character.isdigit() for character in full_name
    )



def enter_student_data(student_list):
    while True:
        full_name = input("Enter the student's full name: ")
        while not is_valid_name(full_name):
            print("Invalid name. Enter a name without numbers.")
            full_name = input("Enter the student's full name: ")

        student_class = input("Enter the student's class: ")
        while not is_valid_section(student_class):
            print("Invalid section. Use a format like 10A or 11B.")
            student_class = input("Enter the student's class: ")

        student_class = student_class.upper()

        if student_exists(student_list, full_name, student_class):
            print("This student is already registered in this section.")
        else:
            break

    spanish_grade = validate_grade("Spanish")
    english_grade = validate_grade("English")
    social_studies_grade = validate_grade("Social Studies")
    science_grade = validate_grade("Science")

    student_data = Student(
        full_name,
        student_class,
        spanish_grade,
        english_grade,
        social_studies_grade,
        science_grade
    )

    return student_data

def validate_grade(subject):
    while True:
        try:
            grade = int(input(f"Enter the {subject} grade (0-100):"))

            if grade < 0 or grade > 100:
                print("Invalid grade. Enter a number between 0 and 100.")
            else:
                return grade
        except ValueError:
            print("Invalid input. Please enter a number.")


def student_information(student_list):
    if not student_list:
        print("No students registered yet.")
        return

    for student in student_list:
        print("Name:", student.name)
        print("Section:", student.section)
        print("Spanish:", student.spanish_grade)
        print("English:", student.english_grade)
        print("Social Studies:", student.social_studies_grade)
        print("Science:", student.science_grade)

def top_GPA_students(student_list):
    if len(student_list) == 0:
        print("No students registered yet.")
        return

    student_averages = []

    for student in student_list:
        average = (
            student.spanish_grade
            + student.english_grade
            + student.social_studies_grade
            + student.science_grade
        ) / 4

        student_average = {
            "full_name": student.name,
            "average": average
        }

        student_averages.append(student_average)

    sorted_students = sorted(
        student_averages,
        key=lambda student: student["average"],
        reverse=True
    )

    top_three = sorted_students[:3]

    for student in top_three:
        print(f"{student['full_name']}: {student['average']:.2f}")

def grade_point_average(student_list):
    if len(student_list) == 0:
        print("No students registered yet.")
        return

    total_average = 0

    for student in student_list:
        average = (
            student.spanish_grade
            + student.english_grade
            + student.social_studies_grade
            + student.science_grade
        ) / 4

        total_average += average

    general_average = total_average / len(student_list)
    print(f"General average: {general_average:.2f}")


def delete_student_info(student_list, full_name, student_class):
    for student in student_list:
        if (
            student.name.lower() == full_name.lower()
            and student.section.lower() == student_class.lower()
        ):
            confirmation = input(
                f"Are you sure you want to delete {full_name} from {student_class}? (yes/no): "
            )

            if confirmation.lower() == "yes":
                student_list.remove(student)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


def underperforming_students(student_list):
    if len(student_list) == 0:
        print("No students registered yet.")
        return

    found_students = False

    for student in student_list:
        if (
            student.spanish_grade < 60
            or student.english_grade < 60
            or student.social_studies_grade < 60
            or student.science_grade < 60
        ):
            found_students = True

            print(student.name)
            print(student.section)

            if student.spanish_grade < 60:
                print(f"Spanish: {student.spanish_grade}")

            if student.english_grade < 60:
                print(f"English: {student.english_grade}")

            if student.social_studies_grade < 60:
                print(f"Social Studies: {student.social_studies_grade}")

            if student.science_grade < 60:
                print(f"Science: {student.science_grade}")

    if not found_students:
        print("No failing students found.")


def exit_program():
    print("Exiting the student management system. Goodbye!")
    sys.exit()

