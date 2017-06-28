import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity import *
from utils.coord import Coord

class Item(Entity):

    def __init__(self,coords,width,height,name,points):
        super(Item,self).__init__(coords,width,height)
        self.name = name
        self.points = points

    def update(self):
        print("Item update")
