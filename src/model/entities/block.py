from entity import Entity

class Block(Entity):
    """auteur: Julien-182

    Cette classe représente les blocks composant le terrain des niveaux
    """

    def __init__(self,coords,width,height,passThroughTop=False,passThroughBottom=False):
        """
        Constructeur de la classe Block

        :param coords: Coordonnées du block sur le niveau
        :param width: largeur du block
        :param height: hauteur du block
        :param passThroughTop: Un Character peu passer à travers le haut du block
        :param passThroughBottom: Un Character peu passer à travers le bas du block
        :type coord: Coord
        :type width: int
        :type height: int
        :type passThroughTop: Boolean
        :type passThroughBottom: Boolean
        :return: objet de type Block
        :rtype: Block
        """
        super(Block, self).__init__(coords,width,height)
        self.passThroughTop = passThroughTop
        self.passThroughBottom = passThroughBottom
