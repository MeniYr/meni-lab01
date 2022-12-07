from animal import Animal

class Dog(Animal):
    def __init__(self, km):
        super().__init__()
        self.km = km

    def run(self):
        print('dog run km: ' + str(self.km) )

    def dogmaokesound(self):
       super().makesound('hav hav!')

    def move(self):
        print('dog move')