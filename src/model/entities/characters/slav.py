import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from character import *

class Slav(Character):

    def __init__(self,coords,width,height,maxHealthPoints,attackPoints):
        super(Slav, self).__init__(coords,width,height,maxHealthPoints)
        self.attackPoints = attackPoints

    def attack(enemy):
        enemy.takeDammages(self.attackPoints)
