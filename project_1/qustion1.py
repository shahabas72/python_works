x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(len(x)):
    if i%2!=0:
        x[i]='&'
x.reverse()
print(x)
