import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity import *

class Character(Entity):

    def __init__(self,coords,width,height,maxHealthPoints):
        super(Character, self).__init__(coords,width,height)
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = maxHealthPoints
        self.touchTop=False
        self.touchBottom=False
        self.touchLeft=False
        self.touchRight=False

    def takeDammages(self,dammages):
        self.healthPoints-=dammages
        if self.healthPoints < 0:
            self.healthPoints = 0
