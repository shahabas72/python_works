a=[1,1,2,3,4,5]
max=0
most_element=0
for i in range(len(a)):
    c=a.count(a[i])
    if c > max:
        most_element=a[i]
        max=c
if max > 1:
    print("most repeating element:",most_element)
else:
    print("No repeating elements")