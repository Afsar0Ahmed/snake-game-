n = 18
guss_chance = 0
guss = int(input("enter the number "))


while guss !=n:
    if guss == n:
        print("you ar won the game ")
        guss_chance = guss_chance + 1
        break

    elif guss < n:
        print("your numbe ris so small")
        guss_chance = guss_chance + 1
        continue

    elif guss > n:
        print("your number is so big")
        guss_chance = guss_chance + 1
        continue

    else:
        print("your typing is string number")















