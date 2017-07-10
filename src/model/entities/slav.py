from character import Character

class Slav(Character):
    """auteur: Julien-182

    Classe représentant le personnage du joueur
    """

    def __init__(self,coords,width,height,maxHealthPoints,attackPoints):
        """
        Constructeur de la classe Slav

        :param coords: Coordonnées du enemy sur le niveau
        :param width: largeur du slav
        :param height: hauteur du slav
        :param maxHealthPoints: nombre de points de vie maximum du Slav
        :param attackPoints: nombre de point d'attaque du slav
        :type coords: Coord
        :type width: int
        :type height: int
        :type maxHealthPoints: int
        :type attackPoints: int
        :return: objet de type Slav
        :rtype: Slav
        """
        super(Slav, self).__init__(coords,width,height,maxHealthPoints)
        self.attackPoints = attackPoints
        self.drunk = False
