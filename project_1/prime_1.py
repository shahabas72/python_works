a=int(input('Enter a limit: '))
b=[]
for i in range(1,a+1):
    count = 0
    x=i
    for m in range(1,a+1):
        if x%m==0:
            count=count+1
    if count==2:
        b.append(x)
print(b)
