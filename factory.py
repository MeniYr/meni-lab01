class Cola(object):
    def drink(self):
        print('Drink cola')

class Sprite(object):
    def drink(self):
        print('Sprite Sprite')

class Fact(object):
    def __init__(self, x):
        self.x = x


    def getobject(self):
        if self.x > 10:
            return Cola()
        else:
            return Sprite()