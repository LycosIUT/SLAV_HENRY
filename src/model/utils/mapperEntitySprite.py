class MapperEntitySprite(object):

    sprites = {}

    @staticmethod
    def getSpriteOfEntity(entityType):
        return sprites[type]

    @staticmethod
    def setSpriteOfEntity(entityType,pathToSprite):
        if entityType not in sprites:
            sprites[entityType] = [pathToSprite]
