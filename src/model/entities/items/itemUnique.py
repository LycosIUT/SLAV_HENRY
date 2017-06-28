from item import Item
from utils.coord import Coord

class ItemUnique(Item):

    def __init__(self,coords,width,height,name,points):
        super(ItemUnique, self).__init__(coords,width,height,name,points)
