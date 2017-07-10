from entity import Entity

class Block(Entity):
    """auteur: Julien-182

    Cette classe représente les blocks composant le terrain des niveaux
    """

    def __init__(self,coords,width,height,canPassThroughTop=False,canPassThroughBottom=False):
        """
        Constructeur de la classe Block

        :param coords: Coordonnées du block sur le niveau
        :param width: largeur du block
        :param height: hauteur du block
        :param passThroughTop: Un Character peut passer à travers le haut du block
        :param passThroughBottom: Un Character peut passer à travers le bas du block
        :type coords: Coord
        :type width: int
        :type height: int
        :type canPassThroughTop: Boolean
        :type canPassThroughBottom: Boolean
        :return: objet de type Block
        :rtype: Block
        """
        super(Block, self).__init__(coords,width,height)
        self.canPassThroughTop = canPassThroughTop
        self.canPassThroughBottom = canPassThroughBottom
