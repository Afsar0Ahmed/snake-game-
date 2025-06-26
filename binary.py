def search(list,key):
    n=-1
    for i in list:
        n+=1
        if i==key:
            print("th eelemnt is found" ,n,"position")


list = (10,7,4,19,23,100)
key = int(input("entre the key"))


search(list,key)





