a=[1,1,1,2,3,3,4,5]
b=[]
d=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count=count+1
    if count==2:
        b.append(a[i])
    if count==1:
        d.append(a[i])
c=set(b)
print(c,"is repeated in two times")
print("Unique vaules are:",d)
i=len(d)
print("Total number of unique elements is:",i)

