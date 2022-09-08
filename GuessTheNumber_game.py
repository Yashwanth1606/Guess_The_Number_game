import random

randomnumber = random.randint(1,100)
# print(randomnumber)
userguess = None
guess = 0
list1 = []

while(userguess != randomnumber):
    userguess = int(input("Enter your guess :"))
    list1.append(userguess)
    guess += 1
    if(userguess > randomnumber):
        print("You gussed it wrong! Enter lower number")
    elif(userguess < randomnumber):
        print("You gussed it wrong! Enter higher number")
    else:
        print("You gussed it right..........")

print(f"you gussed the right answer in {guess} gusses")
print(f"This are all gusses the user had gused {list1}")