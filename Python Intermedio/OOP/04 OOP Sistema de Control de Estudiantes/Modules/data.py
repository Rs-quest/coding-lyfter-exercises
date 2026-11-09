import csv
from student import Student

def export_data(student_list):
    if not student_list:
        print("No hay estudiantes para exportar.")
        return

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "full_name",
            "student_class",
            "spanish_grade",
            "english_grade",
            "social_studies_grade",
            "science_grade"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in student_list:
            student_data = {
                "full_name": student.name,
                "student_class": student.section,
                "spanish_grade": student.spanish_grade,
                "english_grade": student.english_grade,
                "social_studies_grade": student.social_studies_grade,
                "science_grade": student.science_grade
            }

            writer.writerow(student_data)

    print("Students exported successfully!")

def import_data():
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            student_list = list(reader)

        imported_students = []

        for student in student_list:
            student_data = Student(
                student["full_name"],
                student["student_class"],
                int(student["spanish_grade"]),
                int(student["english_grade"]),
                int(student["social_studies_grade"]),
                int(student["science_grade"])
            )

            imported_students.append(student_data)

        print("Students imported successfully!")
        return imported_students

    except FileNotFoundError:
        print("No saved student file was found.")
        return None