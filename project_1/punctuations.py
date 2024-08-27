#unique
a=[1,2,3,4,5,5,6,6,6]
b=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i] == a[j]:
            count=count+1
    if count == 1:
        b.append(a[i])
c=len(b)
print(c)
print(b)
