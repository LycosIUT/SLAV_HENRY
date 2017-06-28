class Entity(object):

    def __init__(self,coords,width,height):
        super(Entity, self).__init__()
        self.coords = coords
        self.width = width
        self.height = height

    def update():
        print("Entity update")
