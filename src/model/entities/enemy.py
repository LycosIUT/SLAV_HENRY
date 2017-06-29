from character import Character

class Enemy(Character):
    """auteur: Julien-182

    Classe représentant les personnages enemis du joueur
    """

    def __init__(self,coords,width,height,maxHealthPoints,attackPoints):
        """
        Constructeur de la classe Enemy

        :param coords: Coordonnées du enemy sur le niveau
        :param width: largeur de l'enemy
        :param height: hauteur de l'enemy
        :param maxHealthPoints: nombre de points de vie maximum du Enemy
        :param attackPoints: nombre de point d'attaque de l'enemy
        :type coord: Coord
        :type width: int
        :type height: int
        :type maxHealthPoints: int
        :type attackPoints: int
        :return: objet de type Enemy
        :rtype: Enemy
        """
        super(Enemy, self).__init__(coords,width,height,maxHealthPoints)
        self.attackPoints = attackPoints
