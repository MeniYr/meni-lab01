# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from animal import Animal
from dog import Dog
from bird import Bird
from person import Person
from singleton import SinglrtonClass
from factory import Fact
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = Dog(10)
#     a.sleep(3)
#     a.run()
#     a.dogmaokesound()
    # b = Animal()
    # b.sleep(4)

    c = Bird(5)
    c.flying()
    c.birdmakenoise()

# a.move()
# c.move()

# r = Fact(10)
# x = r.getobject()
# x.drink()

# obj1 = SinglrtonClass()
# print(obj1)
# obj2 = SinglrtonClass()
# print(obj2)

p = Person()

