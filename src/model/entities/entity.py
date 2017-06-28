import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.coord import Coord

class Entity(object):

    def __init__(self,coords,width,height):
        super(Entity, self).__init__()
        self.coords = coords
        self.width = width
        self.height = height

    def update(self):
        print("Entity update")
