import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database_2"
)

mycursor = mydb.cursor()

def show_employee():
    mycursor.execute("select * from employee")
    val = mycursor.fetchall()
    for x in val:
        print(x)

def insert_employee():
    nam = input("Enter your name: ")
    pas = input("Enter your password: ")
    phn = input("Enter phone number: ")
    eml = input("Enter your email: ")

    check_sql = "SELECT * FROM employee WHERE name = %s AND password = %s"
    mycursor.execute(check_sql, (nam, pas))
    check = mycursor.fetchall()

    if check:
        print("Password and username already exists")
    else:
        sql = "INSERT INTO employee (name, password, phone_number, email) VALUES (%s, %s, %s, %s)"
        val = (nam, pas, phn, eml)
        mycursor.execute(sql, val)
        print("Employee account created successfully")

    mydb.commit()
def update_employee():
    while True:
        emp_id = input("Enter the employee ID to update: ")

        sql = "SELECT emp_id from employee where emp_id = %s"
        val = (emp_id,)
        mycursor.execute(sql, val)
        ab = mycursor.fetchone()

        if ab:
            print("\nMenu:")
            print("1. Update Name")
            print("2. Update Password")
            print("3. Update Phone Number")
            print("4. Update Email")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_name = input("Enter the new name: ")

                sql = "UPDATE employee SET name = %s WHERE emp_id = %s"
                values = (new_name, emp_id)

                mycursor.execute(sql, values)
                mydb.commit()

                print("Employee ID" ,emp_id, "Updated successfully.")
                break

            elif choice == 2:
                new_pas = input("Enter the new password: ")

                sql = "UPDATE employee SET password = %s WHERE emp_id = %s"
                values = (new_pas, emp_id)

                mycursor.execute(sql, values)
                mydb.commit()

                print("Employee ID" ,emp_id, "Updated successfully.")
                break

            elif choice == 3:
                new_phn = input("Enter the new phone number: ")

                sql = "UPDATE employee SET phone_number = %s WHERE emp_id = %s"
                values = (new_phn, emp_id)

                mycursor.execute(sql, values)
                mydb.commit()

                print("Employee ID" ,emp_id, "Updated successfully.")
                break

            elif choice == 4:
                new_eml = input("Enter the new Email: ")

                sql = "UPDATE employee SET email = %s WHERE emp_id = %s"
                values = (new_eml, emp_id)

                mycursor.execute(sql, values)
                mydb.commit()

                print("Employee ID" ,emp_id, "Updated successfully.")
                break

            elif choice == 5:
                print("You are Exit.")
                break

            else:
                print("Invalid choice. Please try again.")
        else:
            print("Enter a valid ID ")
            break

def delete_employee():
    emp_id = int(input("Enter the employee ID to delete: "))
    delete_query = "DELETE FROM employee WHERE emp_id = %s"
    val = (emp_id,)

    mycursor.execute(delete_query, val)

    mydb.commit()
    if mycursor.rowcount > 0:
        print(mycursor.rowcount, "Record deleted")
    else:
        print("No record found with the given ID.")

while True:
    print("\nMenu:")
    print("1. Insert Employee Details")
    print("2. Show Employee Details")
    print("3. Update Employee Details")
    print("4. Delete Employee")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        insert_employee()
    elif ch == 2:
        show_employee()
    elif ch == 3:
        update_employee()
    elif ch == 4:
        delete_employee()
    elif ch == 5:
        print("You are Exit")
        break
    else:
        print("Invalid choice. Please try again.")

mycursor.close()
mydb.close()