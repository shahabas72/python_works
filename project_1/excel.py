import os
import pandas as pd
def create():
    a = input("Enter a user name: ")
    b = input("Enter a password: ")
    df = pd.DataFrame({'Name': [a], 'Password': [b]})
    if os.path.exists('sample.csv'):
        df.to_csv('sample.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('sample.csv', index=False, header=True)
def login():
    na = input("Enter your name: ")
    pas = int(input("Enter the password: "))
    df = pd.read_csv("sample.csv")
    if ((df['Name'] == na) & (df['Password'] == pas)).any():
        print("Login successful!")
        exit()
    else:
        print("Login failed. Invalid name or password.")

while True:
    ch = int(input('* Enter 1 to create user\n* Enter 2 to Login\n* Enter 3 to Exit\nSelect your Option:'))
    if ch == 1:
        create()
    elif ch == 2:
        login()
    elif ch == 3:
        exit()




