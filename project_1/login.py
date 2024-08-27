d={}
d["name"]=input("Create Your Username: ")
d["pass1"]=input("Create Your Password: ")
print(d)
name1=input("Enter Your UserName: ")
pas=input("Enter Your Password: ")
if name1==d["name"] and d["pass1"]==pas:
    print("Login Succesfull")
else:
    print("Enter correct Password and Username")
