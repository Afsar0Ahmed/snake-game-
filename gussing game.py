n = 10
chance = 0
num = int(input("enter the number"))

while chance<3:
    chance = chance + 1
    break



if num==n:
    print("you won the game ")

elif num>n:
    print("your number is  big than the actual number")
elif num<n:
    print("your number is small than the actual number")
else:
    print("your try over")


