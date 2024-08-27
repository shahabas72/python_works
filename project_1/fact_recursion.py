a=int(input("Enter a number: "))
def facts(a):
    if a<0:
        print("enter a positive number")
    elif a==0:
        return 1
    else:
        fact=a*facts(a-1)
        return fact
print(facts(a))

