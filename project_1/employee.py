import re
import os
while True:
    ch = int(input("* Enter 1 to add employee details\n* Enter 2 to Delete file\n* Enter 3 to Exit\nSelect your Option: "))
    if ch == 1:
        while True:
            name = input("Enter Employee Name: ")
            if os.path.exists(name):
                print("File name already exist using another name")
            elif re.findall("[0-9]", name):
                print("Employee name not contain numeric values")
            else:
                f = open(name, "w")
                f.write(name)
                break
        while True:
            email = input("Enter your email id: ")
            if re.findall("^[a-zA-Z0-9. _%+-]+@[a-zA-Z0-9. -]", email):
                f.write("\n"+email)
                break
            else:
                print("Enter correct email")
        while True:
            phone = input("Enter your phone number: ")
            if re.findall("^\\d{10}$", phone):
                f.write("\n"+phone)
                break
            else:
                print("Enter correct phone number")
    if ch == 2:
        d = input("Enter the file name: ")
        if os.path.exists(d):
            os.remove(d)
            print("Successfully Deleted")
        else:
            print("The file does not exist")
    if ch == 3:
        exit()