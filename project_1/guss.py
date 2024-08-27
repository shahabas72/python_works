import random
c = random.randint(1,10)
print(c)
print("Welcome to the Guess Game")
for i in range(3):
    a = int(input("Enter any number: "))
    if a<c:
        print("Number is Low")
    elif a>c:
        print("Number is high")
    elif a==c:
        print("YOU WIN THE GAME")
        break
else:
    print("YOU LOSS")

