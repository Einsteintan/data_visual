from random import randint

class Die():
    ''' generate a die class '''

    def __init__(self,num_sides=6):
        ''' initialize the attributes '''
        self.num_sides = num_sides
    
    def roll(self):
        ''' return a random value in [1,num_sides] '''
        return randint(1,self.num_sides)