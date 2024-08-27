age=[]
amount=0
for i in range(3):
    c=int(input("* Enter 1 to Continue\n* Enter 2 to Exit\nSelect your Option: "))
    if c==1:
        a=int(input("Enter the age: "))
        if a > 0 and a <= 120:
            age.append(a)
        else:
            print("enter age between 1-120")
            b=int(input("enter age again: "))
            age.append(b)
    if c==2:
        break
for x in range(len(age)):
    if age[x] <= 17:
        amount += 200
    elif age[x] >= 40:
        amount += 300
    else:
        amount += 400
print('Total Ernings:',amount)