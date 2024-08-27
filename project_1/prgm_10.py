s = input("Enter a string: ")
count1 = s.count("*")
count2 = s.count("#")
if count1 > 0 or count2 > 0:
    if count1 > count2:
        print("Possitive Integer")
    elif count2 > count1:
        print("Negative Integer")
    elif count1 == count2:
        print("Valid String")
else:
    print("invalid string")
