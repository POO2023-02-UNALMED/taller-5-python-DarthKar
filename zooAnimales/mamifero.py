from animal import Animal
class Mamifero(Animal):
    cantidadMamiferos=0
    cantidadLeones=0
    cantidadCaballos=0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.cantidadMamiferos+=1

    def CrearCaballo(self,nombre,edad,genero):
        super().__init__(nombre,edad,"pradera",genero)
        self._pelaje = True
        self._patas = 4
        Mamifero.cantidadMamiferos+=1
        Mamifero.cantidadCaballos+=1
    
    def CrearLeon(self,nombre,edad,genero):
        super().__init__(nombre,edad,"selva",genero)
        self._pelaje = True
        self._patas = 4
        Mamifero.cantidadMamiferos+=1
        Mamifero.cantidadLeones+=1
        

    @classmethod
    def cantidadMamiferos(cls):
        return cls.cantidadMamiferos
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas