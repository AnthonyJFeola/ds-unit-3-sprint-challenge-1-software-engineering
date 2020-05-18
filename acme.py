from random import randint
class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal_factor = self.price/self.weight
        if steal_factor < 0.5:
            print('Not so stealable...')
        elif (steal_factor >= 0.5) and (steal_factor < 1.0):
            print('Kinda stealable.')
        else:
            print('Very stealable!')

    def explode(self):
        explode_factor = self.flammability * self.weight
        if explode_factor < 10:
            print('...fizzle.')
        elif (explode_factor >= 10) and (explode_factor < 50):
            print('...boom!')
        else:
            print('...BABOOM!!')

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight, flammability=flammability, identifier=identifier)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        punch_factor = self.weight
        if punch_factor < 5:
            print('That tickles.')
        elif (punch_factor >= 5) and (punch_factor < 15):
            print('Hey that hurt!')
        else:
            print('OUCH!')
