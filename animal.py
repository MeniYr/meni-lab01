# object => הורשה מאובייקט מסויים
import abc
from abc import abstractmethod

class Animal(abc.ABC, object):
    # __ => private varible, def => public
    __name = ''

    def __init__(self):
        self.time = 0

    # self => this
    # אם לא נשים self אז זה static
    def sleep(self, time):
        print('sleep in hours:', time)

    def makesound(self, sound):
        self.sound = sound
        print(self.sound)

    @abstractmethod
    def move(self):
        pass