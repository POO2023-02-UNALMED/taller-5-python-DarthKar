class Zona:

    def __init__(self,nombre,zoo=None):
        
        self._nombre = nombre
        self._zoologico = zoo
        self._animales= []

    def agregarAnimales(self,animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)

    def setNombre(self,nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setZoologico(self,zoo):
        self._zoologico = zoo
    def getZoologico(self):
        return self._zoologico
    
    def setAnimales(self,animales):
        self._animales = animales
    def getAnimales(self):
        return self._animales