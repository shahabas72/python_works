a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x=[]
for i in a:
    if i%2!=0 and i%3==0:
        x.append(i)
b=sum(x)
print(b)