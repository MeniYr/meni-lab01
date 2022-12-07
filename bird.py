from animal import Animal

class Bird(Animal):
    def __init__(self, km):
        super().__init__()
        self.__km = km

    def flying(self):
        print('im flyying!! (for ', self.__km, ' km)')

    def birdmakenoise(self):
        super().makesound('twink twink!')

    def move(self):
        print('bird move')
