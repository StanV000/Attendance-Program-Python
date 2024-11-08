import Function_Validation
from datetime import datetime


def module_record_system_login(information) -> bool:
    """
    A function to get the username/password, ask user for username/password, check if correct.
    :param information: This is the data for the username/password
    :return: True/False for password.
    """
    while True:
        print("Module Record System - Login")
        print("-" * 20)
        username = []
        password = []
        for index, value in enumerate(information):
            value = value.split(",")
            username.append(value[0])
            password.append(value[1].strip())
        while True:
            login_name = input("Name: ")
            if login_name != '':
                break
            else:
                print("Enter a value in!")
        while True:
            login_password = input("Password: ")
            if login_password != '':
                break
            else:
                print("Enter a value in!")

        if login_name in username:
            index = username.index(login_name)
            if password[index] == login_password:
                print(f"Welcome {username[0]}")
                return True
        print()
        print("Login Failed.")
        print("Exiting Module Record System")
        return False


def options_menu() -> int:
    """
    Takes in true or false, and then does a while loop, asking the user for an int, input, and then does an if 
    statement choosing which option it wants. 
    returns the option.
    """
    while True:
        print("Module Record System - Options")
        print("-" * 40)
        print("1. Record Attendance")
        print("2. Generate Statistics")
        print("3. Exit")
        which_option = Function_Validation.read_positive_int_in_range(">", 1, 3)
        return which_option


def load_modules():
    """
    just puts the data from module into seperate lists
    :return: module code and name returned.
    """
    with open("modules.txt", "r") as source4:
        module_data = source4.readlines()

    module_code5 = []
    module_name5 = []
    for index, value in enumerate(module_data):
        value = value.strip().split(",")
        module_code5.append(value[0])
        module_name5.append(value[1])

    return module_code5, module_name5


def Record_attendances_screen_choosing_module(module_code_for_attendance_choosing) -> int:
    """
    Takes parameter and then ask user for an input on which module to choose
    :param module_code_for_attendance_choosing: txt
    :return:  Returning the number of which module user chose.
    """
    print("Module Record System - Attendance - Choose a module")
    print("-" * 40)
    for index, value in enumerate(module_code_for_attendance_choosing):
        print(f"{index + 1}. {value}")
    pick_module = Function_Validation.read_positive_int_in_range(">", 1, len(module_code_for_attendance_choosing))
    return pick_module


def module_attendance(information_about_students1):
    """
    Created 3 empty lists and then enumerated through all and split each value from SOFT_6017 into the 3 lists,
    one for names, present and absent. Returning the three lists.
    """

    Present_days = []
    Absent_days = []
    Name_of_student = []
    for index, value in enumerate(information_about_students1):
        value = value.split(",")
        Name_of_student.append(value[0])
        Present_days.append(int(value[1]))
        Absent_days.append(int(value[2]))
    return Name_of_student, Present_days, Absent_days


def Attendance_of_module_chosen(Name_of_student: list[str], Present_days: list[int], Absent_days: list[int],
                                module_code6: str):
    """
    Given 3 lists, and module pick integer, we create 2 empty list, to then put the original values into those lists,
    and then upddate them accordingly
    We then return the lists.

    """
    updated_present_list = []
    updated_absent_list = []
    for i in Present_days:
        updated_present_list.append(int(i))
    for i in Absent_days:
        updated_absent_list.append(int(i))
    print(f"Module Record System - Attendance -{module_code6} ")
    print("-" * 40)
    print(f"There are {len(Name_of_student)} students enrolled")
    print()
    for index, value in enumerate(Name_of_student):
        print(f"Student {index + 1}: {value}")
        print("1. Present")
        print("2. Absent")
        Option_for_attendance = Function_Validation.read_positive_int_in_range(">", 1, 2)
        if Option_for_attendance == 1:
            updated_present_list[index] += 1
        elif Option_for_attendance == 2:
            updated_absent_list[index] += 1
    return updated_present_list, updated_absent_list


def info_for_students_option_2(information_for_students2):
    """
    gets the data, puts them in a list
    :param information_for_students2:  data of students
    :return:  returns three lists
    """
    Present_days = []
    Absent_days = []
    Name_of_student = []
    for index, value in enumerate(information_for_students2):
        value = value.split(",")
        Name_of_student.append(value[0])
        Present_days.append(int(value[1]))
        Absent_days.append(int(value[2]))
    return Name_of_student, Present_days, Absent_days


def statistics_for_choice_2(module_code1: list[str], module_name2: list[str]):
    """Two Lists, counting total days, number of days present, then calculate attandance rate, then make it all into
    a string accumulator and print at the end, after that print to a file, """
    string_accumulator = ""
    counter = []
    number_of_days_present = []
    for index, value in enumerate(module_code1):
        counter.append(0)
        number_of_days_present.append(0)
        with open(f"{value}.txt", "r") as source5:
            information_about_module = source5.readlines()
            for line in information_about_module:
                student_stuff = line.strip().split(",")
                total = int(student_stuff[1]) + int(student_stuff[2])
                counter[index] += total
                number_of_days_present[index] += int(student_stuff[1])

    string_accumulator += "Module Record System - Average Attendance Data\n"
    string_accumulator += "-" * 40
    string_accumulator += "\n"
    biggest = 0
    biggest_name = ""
    lowest_names = []
    attendance_rate_list = []
    for index, value in enumerate(module_code1):
        attendance_rate_of_student = (number_of_days_present[index] / counter[index]) * 100
        attendance_rate_list.append(attendance_rate_of_student)
        stars = int(attendance_rate_of_student / 10) * "*"
        string_accumulator += f"{module_name2[index]} {value} {attendance_rate_of_student:.0f}% [ {stars} ]\n"
        if attendance_rate_of_student > biggest:
            biggest = attendance_rate_of_student
            biggest_name = module_name2[index]

        if attendance_rate_of_student < 40:
            lowest_names.append(module_name2[index])

    string_accumulator += "\n"
    string_accumulator += f"The best attended module is {biggest_name} with a {biggest:.0f}% attendance rate!\n"
    string_accumulator += "\n"
    if len(lowest_names) > 0:
        string_accumulator += f"There is {len(lowest_names)} module(s) with attendance rate under 40% \n"
        for i in lowest_names:
            string_accumulator += " " + " " + " " + i
            string_accumulator += "\n"

    string_accumulator += "\n"
    today = datetime.today().strftime('%Y_%m_%d')
    with open(f"Attendance_Stats_{today}", "w") as source6:
        source6.write(string_accumulator)
    print(string_accumulator)
    print(f"The above data is also stored at Attendance_Stats_{today}.txt")
    print()
    input("Press Enter To Continue")


def write_to_a_file_for_student(Name_of_Student: list[str], Present_days: list[int], Absent_days: list[int]):
    """
    Giving the Function  3 Lists, 1 for names, 2 for updated Present Days and Absent Days. Opening file, then looping
    through name of students  and writing the value for each list into file {module_code_chosen}, updating the
    original file.
    """
    with open(f"{module_code_chosen}.txt", "w") as source3:
        for value in range(len(Name_of_Student)):
            source3.write(f"{Name_of_Student[value]},{Present_days[value]},{Absent_days[value]}" + "\n")
    print(f"{module_code_chosen}.txt was updated with the latest attendance records")
    input("Press Enter to Continue")


if __name__ == '__main__':
    try:
        with open("Login_data.txt", "r") as source:
            inside_login = source.readlines()
    except FileNotFoundError:
        print("File was not found!")
    if module_record_system_login(inside_login):
        option = 0
        module_code, module_name = load_modules()
        while option != 3:
            option = options_menu()
            if option == 1:
                pick_module_option = Record_attendances_screen_choosing_module(module_code)
                module_code_chosen = module_code[pick_module_option - 1]
                with open(f"{module_code_chosen}.txt", "r") as source:
                    information_about_students = source.readlines()
                student_name, present, absent = module_attendance(information_about_students)
                Present_Days_updated, Absent_days_updated = Attendance_of_module_chosen(student_name, present, absent,
                                                                                        module_code_chosen)
                write_to_a_file_for_student(student_name, Present_Days_updated, Absent_days_updated)
            elif option == 2:
                statistics_for_choice_2(module_code, module_name)
