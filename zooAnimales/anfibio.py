from zooAnimales.animal import Animal
class Anfibio(Animal):
    canAnfibios=0
    ranas=0
    salamandras=0
    _listado=[]

    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio.canAnfibios+=1
        Anfibio._listado.append(self)
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana=cls(nombre,edad,"selva",genero,"rojo",True)
        Anfibio.ranas+=1
        return rana
    
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra=cls(nombre,edad,"selva",genero, "negro y amarillo",False)
        Anfibio.salamandras+=1
        return salamandra
    
    @classmethod
    def cantidadAnfibios(cls):
        return cls.cantidadAnfibios

    def movimiento(self):
        return "saltar"    
    
    def setListado(self,listado):
        self._listado = listado
    def getListado(self):
        return self._listado
    
    def setColorPiel(self,color):
        self._colorPiel = color
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self,ven):
        self._venenoso=ven
    def isVenenoso(self):
        return self._venenoso


