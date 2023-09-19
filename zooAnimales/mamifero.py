from animal import Animal
class Mamifero(Animal):
    cantidadMamiferos=0
    leones=0
    caballos=0
    _listado=[]
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.cantidadMamiferos+=1
        Mamifero._listado.append(self)

    def crearCaballo(self,nombre,edad,genero):
        super().__init__(nombre,edad,"pradera",genero)
        self._pelaje = True
        self._patas = 4
        Mamifero.cantidadMamiferos+=1
        Mamifero.cantidadCaballos+=1
        Mamifero._listado.append(self)
    
    def crearLeon(self,nombre,edad,genero):
        super().__init__(nombre,edad,"selva",genero)
        self._pelaje = True
        self._patas = 4
        Mamifero.cantidadMamiferos+=1
        Mamifero.cantidadLeones+=1
        Mamifero._listado(self)
        

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