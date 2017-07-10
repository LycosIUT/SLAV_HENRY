from entity import Entity

class Character(Entity):
    """auteur: Julien-182

    Cette classe représente chaque personnage,NPC,enemy du jeu
    """

    def __init__(self,coords,width,height,maxHealthPoints):
        """
        Constructeur de la classe Character

        :param coords: Coordonnées du character sur le niveau
        :param width: largeur du character
        :param height: hauteur du character
        :param maxHealthPoints: nombre de points de vie maximum du Character
        :type coords: Coord
        :type width: int
        :type height: int
        :type maxHealthPoints: int
        :return: objet de type Character
        :rtype: Character
        """
        super(Character, self).__init__(coords,width,height)
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = maxHealthPoints
        self.touchTop = False
        self.touchBottom = False
        self.touchLeft = False
        self.touchRight = False
        self.facingLeft = False;
        self.isDead = False

    def update(self):
        """
        Met à jour l'état du Character
        """
        self.isDead =  (self.healthPoints == 0)

    def takeDammages(self,dammages):
        """
        Affecte des dégâts aux points de vie du Character

        :param dammages: Points de dégâts à infliger
        :type dammages: int
        """
        self.healthPoints -= dammages
        if self.healthPoints < 0:
            self.healthPoints = 0

    def attack(self,enemy):
        """
        Attaque et inflige de dégâts au Character passé en paramètre

        :param enemy: Character à attaquer
        :type enemy: Character
        """
        enemy.takeDammages(self.attackPoints)
