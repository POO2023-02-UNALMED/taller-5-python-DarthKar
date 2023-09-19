from zooAnimales.animal import Animal
class Mamifero(Animal):
    canMamiferos=0
    leones=0
    caballos=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.canMamiferos+=1
        Mamifero._listado.append(self)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = cls(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return caballo

    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        leon = cls(nombre,edad,"selva",genero, True, 4)
        Mamifero.leones+=1
        return leon
    

    @classmethod
    def cantidadMamiferos(cls):
        return cls.cantidadMamiferos
    
    def setListado(self, lista):
        self._listado = lista
    def getListado(self):
        return self._listado

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas