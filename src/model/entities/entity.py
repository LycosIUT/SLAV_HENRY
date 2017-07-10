class Entity(object):
    """auteur : Julien-182

    Cette classe va représenter toutes les entités "physiques" du jeu (blocks,characters,items,...)
    """

    def __init__(self,coords,width,height):
        """
        Constructeur de la classe Entity

        :param coords: Coordonnées de l'entitité sur le niveau
        :param width: largeur de l'entité
        :param height: hauteur de l'entité
        :type coords: Coord
        :type width: int
        :type height: int
        :return: objet de type Entity
        :rtype: Entity
        """
        super(Entity, self).__init__()
        self.coords = coords
        self.width = width
        self.height = height
        self.visible = True

    def update(self):
        """
        Cette fonction met à jour l'état de l'entité
        """
        print("Entity update")
