import re
import os
def reg_details():
    while True:
        name = input("Enter Employee Name: ")
        if os.path.exists(name):
            print("File name already exist using another name")
        elif re.findall("[0-9]", name):
            print("Employee name not contain numeric values")
        else:
            #a += name
            f = open(name, "w")
            f.write(name)
            break
    while True:
        email = input("Enter your email id: ")
        if re.findall("^[a-zA-Z0-9. _%+-]+@[a-zA-Z0-9. -]", email):
            f.write("\n" + email)
            break
        else:
            print("Enter correct email")
    while True:
        phone = input("Enter your phone number: ")
        if re.findall("^\\d{10}$", phone):
            f.write("\n" + phone)
            break
        else:
            print("Enter correct phone number")
def delete():
    d = input("Enter the file name: ")
    if os.path.exists(d):
        os.remove(d)
        print("Successfully Deleted")
    else:
        print("The file does not exist")
while True:
    c=int(input("* Enter 1 to add employee details\n* Enter 2 to Delete file\n* Enter 3 to Exit\nSelect your Option: "))
    if c==1:
        reg_details()
    elif c==2:
        delete()
    elif c==3:
        exit()