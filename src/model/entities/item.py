from entity import Entity

class Item(Entity):
    """auteur: Julien-182

    Classe représentant les items/objets du jeu
    """

    def __init__(self,coords,width,height,name,points):
        """
        Constructeur de la classe Item

        :param coords: Coordonnées de l'item sur le niveau
        :param width: largeur de l'item
        :param height: hauteur de l'item
        :param name: libellé de l'item
        :param points: points que donne de le ramassage de l'item
        :type coord: Coord
        :type width: int
        :type height: int
        :type name: string
        :type points: int
        :return: objet de type Item
        :rtype: Item
        """
        super(Item,self).__init__(coords,width,height)
        self.name = name
        self.points = points

    def update(self):
        """
        Cette fonction met à jour l'état de l'item
        """
        print("Item update")
