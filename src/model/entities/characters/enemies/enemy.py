import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from character import *
from slav import *

class Enemy(Character):

    def __init__(self,coords,width,height,maxHealthPoints,attackPoints):
        super(Enemy, self).__init__(coords,width,height,maxHealthPoints)
        self.attackPoints = attackPoints

    def attack(self,slav):
        slav.takeDammages(self.attackPoints)
