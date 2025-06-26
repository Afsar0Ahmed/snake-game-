# this is concept of inheritance...........
# class Animal :
#     alive  = True
#     def eat(self):
#         print("this is eating fast")
#     def sleep(self):
#         print("this is sleeping ")
# class Rabit(Animal):
#     def speed(self):
#         print("its speed 120km/h")
# class Fish(Animal):
#     pass
# class Hauk(Animal):
#     pass
# rabit  = Rabit()
# rabit.eat()
# rabit.sleep()
# rabit.speed()
# print(rabit.alive)


# Multiple inharitance --->> when a child class derived more than one class.......
class Human:
    def sleep(self):
        print(" can sleep")
    def walk(self):
        print("can  walking ")
class Bird :
    def fly(self):
        print(" can fly")
class Henbird(Human,Bird):
    def sound(self):
        print("can sound")

henbird = Henbird()
henbird.sleep()
henbird.walk()
henbird.fly()
henbird.sound()




