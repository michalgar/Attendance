"""
This file will include the main functionality of the program.
It should display a menu of actions to the user and invoke the relevant function
"""
import Logic
import datetime


def prompt():
    print("\nWhat would you like to do?")
    print("1- Add employee manually")
    print("2- Add employee from file")
    print("3- Delete employee manually")
    print("4- Delete employee from file")
    print("5- Mark attendance")
    print("6- Generate attendance report of an employee")
    print("7- Generate monthly attendance report for all employees")
    print("8- Generate late attendance report")

    action = input("Please select an action by typing its corresponding number: ")
    return action


def main():
    user_action = prompt()
    if user_action == '1':
        name = input("Employee's name: ")
        phone = input("Employee's phone number: ")
        birth = input("Employee's year of birth: ")
        uid = input("Employee's ID: ")
        age = datetime.date.today().year - int(birth)

        # Create an Employee instance and call add_employee()
        new_emp = Logic.Employee(uid, name, phone, age)
        new_emp.add_employee()

    elif user_action == '2':
        file_path = input("Please enter the path of the file with employees to add: ")
        Logic.add_from_file(file_path)

    elif user_action == '3':
        uid_to_delete = input("Please select the UID of the user you'd like to delete: ")
        Logic.delete_emp(uid_to_delete)

    elif user_action == '4':
        file_path = input("Please enter the path of the file with employees to delete: ")
        Logic.delete_from_file(file_path)
    elif user_action == '5':
        pass
    elif user_action == '6':
        pass
    elif user_action == '7':
        pass
    elif user_action == '8':
        pass


if __name__ == '__main__':
    main()
