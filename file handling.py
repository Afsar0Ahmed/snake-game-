# file = open("test.txt","w")
# x = file.write("i am a good boy")
#
# file.close()
file = open("test.txt")
x = ["red", "white", "black"]
for item in x:
    file.write(item+"\n")
    file.close()



