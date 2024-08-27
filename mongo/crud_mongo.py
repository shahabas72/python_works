import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["database_2"]
mycol = mydb["table_1"]

mycol.create_index("phone", unique=True)
def insert():
    name = input("enter your name: ")
    address = input("enter your address: ")
    phone = input("enter your phone number: ")
    password = input("enter your password: ")

    dict={"name": name, "address": address, "phone": phone, "password": password}

    try:
        mycol.insert_one(dict)
        print("Data inserted successfully")
    except pymongo.errors.DuplicateKeyError:
        print("This phone number already exists in the database")

def update():
    while True:
        phone = input("enter your phone number: ")
        query = {"phone": phone}
        x = mycol.find_one(query)
        if x:
            print("\nMenu:")
            print("1. Update Name")
            print("2. Update Password")
            print("3. Update Phone Number")
            print("4. Update Address")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_name = input("Enter the new name: ")
                newdict = {"$set": {"name": new_name}}
                mycol.update_one(query,newdict)
                break
            if choice == 2:
                new_pass = input("Enter the new password: ")
                newdict = {"$set": {"password": new_pass}}
                mycol.update_one(query,newdict)
                break
            if choice == 3:
                new_phn = input("Enter the new phone number: ")
                try:
                    newdict = {"$set": {"phone": new_phn}}
                    mycol.update_one(query, newdict)
                    print("Data updated successfully")
                except pymongo.errors.DuplicateKeyError:
                    print("This phone number already exists in the database")
                break
            if choice == 4:
                new_add = input("Enter the new address: ")
                newdict = {"$set": {"adress": new_add}}
                mycol.update_one(query,newdict)
                break
            if choice == 5:
                print("You are Exit.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Enter a valid phone number")
            break
def delete():
    phone = input("Enter your phone number: ")
    query = {"phone": phone}
    x = mycol.find_one(query)
    if x:
        mycol.delete_one(query)
        print("Data deleted successfully!")
    else:
        print("Enter a valid phone number!")

while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Update")
    print("3. Delete")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        insert()
    elif ch == 2:
        update()
    elif ch == 3:
        delete()
    elif ch == 4:
        print("You are Exit")
        break
    else:
        print("Invalid choice. Please try again.")