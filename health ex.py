def gettime():
    return gettime().datetime.now()
def take(k):
    if k != 1:
        return
    c=int(input("enter 1 for exersice enter 2 for food "))
    if c==1 :
        value=input("type here")
        with open("afsar.txt")as op:
            print("succesfully written")
    elif c==2:
        value=input("type here")
        with open("food.txt")as op:
            print("food timetable")
    else:
        



