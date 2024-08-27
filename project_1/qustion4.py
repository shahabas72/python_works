x=(1,2,3,4,5,6,7,8,9,10)
a=list(x)
for i in range(len(a)):
    if i%7==0:
        a[i]='&'
    if i%2==0:
        a[i]='@'
x=tuple(a)
print(x)