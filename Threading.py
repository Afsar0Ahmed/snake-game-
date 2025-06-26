import  threading
import time


def eat():
    time.sleep(5)
    print("at firdt we eating ")
def coffe():
    time.sleep(6)
    print("it time to drink coffe ")
def study():
    time.sleep(4)
    print("its time to study ")
a  = threading.Thread(target= eat,args=())
a.start()
b  = threading.Thread(target=coffe,args=())
b.start()
c = threading.Thread(target=study , args=())
c.start()

print(threading.enumerate())
print(threading.active_count())


# eat()
# coffe()
# study()

