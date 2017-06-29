from item import Item

class ItemUnique(Item):
    """auteur: Julien-182

    Classe représentant tous les items uniques/bonus rares du jeu
    """

    def __init__(self,coords,width,height,name,points):
        """
        Constructeur de la classe ItemUnique

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
        :return: objet de type ItemUnique
        :rtype: ItemUnique
        """
        super(ItemUnique, self).__init__(coords,width,height,name,points)
