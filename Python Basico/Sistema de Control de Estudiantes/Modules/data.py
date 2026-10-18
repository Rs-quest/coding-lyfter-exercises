import csv


def export_data(student_list):
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
        writer.writerows(student_list)

    print("Students exported successfully!")

def import_data():
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            student_list = list(reader)

        for student in student_list:
            student["spanish_grade"] = int(student["spanish_grade"])
            student["english_grade"] = int(student["english_grade"])
            student["social_studies_grade"] = int(student["social_studies_grade"])
            student["science_grade"] = int(student["science_grade"])

        print("Students imported successfully!")
        return student_list

    except FileNotFoundError:
        print("No saved student file was found.")
        return None