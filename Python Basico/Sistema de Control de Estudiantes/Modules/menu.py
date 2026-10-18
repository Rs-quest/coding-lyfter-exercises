from actions import (
    enter_student_data,
    validate_grade,
    student_information,
    top_GPA_students,
    grade_point_average,
    delete_student_info,
    underperforming_students,
    exit_program
)
from data import export_data, import_data
def show_menu(student_list):
    while True:
        print(
            "1. Enter Student Information\n"
            "2. Note Validation\n"
            "3. Student Information\n"
            "4. Top GPA Students\n"
            "5. Grade Point Average\n"
            "6. Delete Student Info\n"
            "7. Underperforming Students\n"
            "8. Export Students\n"
            "9. Import Students\n"
            "10. Exit"
        )
        
        try:
            option = int(input("Option:"))


            if option == 1:
                number_of_students = int(
                    input("How many students do you want to register? ")
            )

                for i in range(number_of_students):
                    student_data = enter_student_data(student_list)
                    student_list.append(student_data)
    
            elif option == 2:
                print("Grades are validated when registering students.")
    
            elif option == 3:
                student_information(student_list)
    
            elif option == 4:
                top_GPA_students(student_list)
    
            elif option == 5:
                grade_point_average(student_list)
    
            elif option == 6:
                full_name = input("Enter the student's full name: ")
                student_class = input("Enter the student's section: ")

                delete_student_info(
                    student_list,
                    full_name,
                    student_class
                )
    
            elif option == 7:
                underperforming_students(student_list)
    
            elif option == 8:
                export_data(student_list)

            elif option == 9:
                imported_students = import_data()

                if imported_students is not None:
                    student_list.clear()
                    student_list.extend(imported_students)

            elif option == 10:
                exit_program()
        
            else: 
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number")