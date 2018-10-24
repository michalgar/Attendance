import csv
import os
import datetime

employees_csv = 'employees.csv'
employees_temp = 'employees_temp.csv'


class Employee:
    def __init__(self, employee_id, name, phone, age):
        self.uid = employee_id
        self.name = name
        self.phone = phone
        self.age = age

    def add_employee(self):
        # TODO: Validate that all the data is provided
        # TODO: decide if this should happen here on in the init phase
        # TODO: Check if the employee already exists in the file
        # Add new employee data to the file
        with open('employees.csv', 'a', newline='') as employees_file:
            fields = [self.uid, self.name, self.phone, self.age]
            writer = csv.writer(employees_file)
            writer.writerow(fields)


def add_from_file(file):
    with open(file, 'r') as to_add:
        for employee in csv.reader(to_add, delimiter=","):
            if employee[0].isdigit():
                uid = employee[0]
            else:
                print("Invalid UID field- UID must be a number")
                break

            if str(employee[1]).isalpha():
                name = employee[1]
            else:
                print("Invalid name field for UID {0}".format(uid))
                break
                # TODO: consider adding a system to retry/ drop back to main menu

            if employee[2].isdigit and len(employee[2]) == 10:
                phone = employee[2]
            else:
                print("Invalid phone number for UID {0}- phone must consist of 10 digits".format(uid))
                break

            # Discriminating people over  120 years :)
            if employee[3].isdigit:
                age = datetime.date.today().year - int(employee[3])
                if age > 120:
                    print("{0} is {1} years old and still an employee?! Fool me again...".format(name, age))
            else:
                print("Invalid age for UID {0}".format(uid))
                break

            new_emp = Employee(uid, name, phone, age)
            new_emp.add_employee()


# TODO: This function uses constants from the beginning of this file. Reconsider this design decision
def delete_emp(uid):
    # to_add = []
    #
    # with open(employees_csv, 'r') as employees_read:
    #     for row in csv.reader(employees_read):
    #         if row[0] != uid:
    #             to_add.append(row)
    #
    # with open(employees_csv, 'w', newline='') as employees_write:
    #     writer = csv.writer(employees_write)
    #     for line in to_add:
    #         writer.writerow(line)
    with open(employees_csv, 'r') as employees_read, open(employees_temp, 'w', newline='') as employees_write:
        writer = csv.writer(employees_write)
        for row in csv.reader(employees_read):
            if row[0] != uid:
                writer.writerow(row)

    if os.path.exists(employees_csv) and os.path.exists(employees_temp):
        os.remove(employees_csv)
        os.rename(employees_temp, employees_csv)
    else:
        print("File doesn't exist")


def delete_from_file(path):
    with open(path, 'r') as to_delete:
        reader = csv.reader(to_delete)
        for row in reader:
            if row[0].isdigit():
                uid = row[0]
            delete_emp(uid)


def validate(details):
    if len(details) != 4:
        return "You are to supply 4 fields"
    if not details[0].isdigit():
        return "The UID must be numeric"
    if not details[1].isalpha():
        return "Employee name must not contain numbers"
    if not details[2].isdigit and len(details[2]) != 10:
        return "Phone number must contain 10 digits"
    if not details[3].isdigit:
        return "Birth year must be numeric"
    else:
        age = datetime.date.today().year - int(details[3])
        if age > 120:
            return "{0} is {1} years old? Unbelievable!"
    return True


# Checks if an employee exists in the employees file (with all of its data)
def exists(employee_row):
    with open(employees_csv, 'r') as employee_read:
        for row in csv.reader(employee_read):
            if employee_row == row:
                return True
        return False
