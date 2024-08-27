import mysql.connector
from decimal import Decimal

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database3"
)

mycursor = mydb.cursor()

def create_account():
    nam = input("Enter your name: ")
    phn = input("Enter your phone number: ")

    sql = "INSERT INTO bank (account_name, phone) VALUES (%s, %s)"
    val = (nam, phn)
    mycursor.execute(sql, val)
    print("Account created successfully")
    mydb.commit()
def deposit():
    acc_nam = input("Enter your name: ")
    acc_num = input("Enter your account number: ")

    check_sql = "SELECT * FROM bank WHERE account_name = %s AND account_no = %s"
    mycursor.execute(check_sql, (acc_nam, acc_num))
    check = mycursor.fetchall()

    if check:
        deposit_amt = Decimal(input("Enter the amount you want to deposit: "))

        sql = "SELECT balance FROM bank WHERE account_no = %s"
        val = (acc_num,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            current_bal = result[0]
            new_bal = current_bal + deposit_amt

            sql = "UPDATE bank SET balance = %s WHERE account_no = %s"
            val = (new_bal, acc_num)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Deposit of amount",deposit_amt,"is successful \nNew account balance is: ", new_bal)
        else:
            print("Process failed please try again")
    else:
        print("Incorrect account name or account number.")

def withdraw():
    acc_nam1 = input("Enter your name: ")
    acc_num1 = input("Enter your account number: ")

    check_sql = "SELECT * FROM bank WHERE account_name = %s AND account_no = %s"
    mycursor.execute(check_sql, (acc_nam1, acc_num1))
    check = mycursor.fetchall()

    if check:
        withdraw_amt = Decimal(input("Enter the amount you want to withdraw: "))

        sql = "SELECT balance FROM bank WHERE account_no = %s"
        val = (acc_num1,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            current_bal = result[0]
            minimum_balance = Decimal('1000.00')

            if withdraw_amt > current_bal:
                print("Insufficient balance!")
            elif current_bal - withdraw_amt < minimum_balance:
                print("Cannot withdraw. Minimum balance of",minimum_balance,"must be maintained.")
            else:
                new_bal = current_bal - withdraw_amt

                sql = "UPDATE bank SET balance = %s WHERE account_no = %s"
                val = (new_bal, acc_num1)
                mycursor.execute(sql, val)
                mydb.commit()

                print("Withdrawal of amount", withdraw_amt, "is successful \nNew account balance is: ", new_bal)
        else:
            print("Transaction failed, please try again.")
    else:
        print("Incorrect account name or account number.")

def balance():
    acc_nam = input("Enter your name: ")
    acc_num = input("Enter your account number: ")

    check_sql = "SELECT * FROM bank WHERE account_name = %s AND account_no = %s"
    mycursor.execute(check_sql, (acc_nam, acc_num))
    check = mycursor.fetchall()

    if check:
        sql = "SELECT balance FROM bank WHERE account_no = %s"
        val = (acc_num,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            current_bal = result[0]
            print("Current balance is: ", current_bal)
        else:
            print("Failed to retrieve balance. Please try again!")
    else:
        print("Incorrect account name or account number.")

while True:
    print("\nMenu:")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Check balance")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        balance()
    elif choice == 5:
        print("You are exit")
        break
    else:
        print("Invalid choice. Please try again")
