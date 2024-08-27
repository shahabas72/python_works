i=1
fact=1
n=int(input("Enter the limit: "))
while i<=n:
    fact=fact*i
    i+=1
print("factorial of",n,"is",fact)


"""def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)"""