"""
This file will include the main functionality of the program.
It should display a menu of actions to the user and invoke the relevant function
"""
import Logic

# Display a menu to the user
print("\nWhat would you like to do?")
print("1- Add employee")
print("2- Delete employee")
print("3- Mark attendance")
print("4- Generate a report")

user_action = input("Please select an action by typing its corresponding number: ")

# Sub-action
if user_action == '1':
    print("\nYou chose to add employee.\nPlease select one of the methods below:")
    print("1- Add employee manually")
    print("2- Add employee from file")
    sub_action = input("Please select an action by typing its corresponding number: ")
    if sub_action == '1':
        Logic.Employee.add_employee()

elif user_action == '2':
    print("\nYou chose to delete employee.\nPlease select one of the methods below:")
    print("1- Delete employee manually")
    print("2- Delete employee from file")
    sub_action = input("Please select an action by typing the corresponding number: ")

elif user_action == '3':
    pass
elif user_action == '4':
    print("\nYou chose to generate report.\nPlease select one of the methods below:")
    print("1- Generate attendance report of an employee")
    print("2- Generate monthly attendance report for all employees")
    print("3- Generate late attendance report")
    sub_action = input("Please select an action by typing the corresponding number: ")
