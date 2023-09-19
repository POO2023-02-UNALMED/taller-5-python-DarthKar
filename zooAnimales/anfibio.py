from zooAnimales.animal import Animal
class Anfibio(Animal):
    cantidadAnfibios=0
    ranas=0
    salamandras=0
    _listado=[]

    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio.cantidadAnfibios+=1
        Anfibio._listado.append(self)
    
    def crearRana(self,nombre,edad,genero):
        super().__init__(nombre,edad,"selva",genero)
        self._colorPiel="rojo"
        self._venenoso=True
        Anfibio.cantidadAnfibios+=1
        Anfibio.ranas+=1
        Anfibio._listado.append(self)
    
    def crearSalamandra(self,nombre,edad,genero):
        super().__init__(nombre,edad,"selva",genero)
        self._colorPiel= "negro y amarillo"
        self._venenoso= False
        Anfibio.cantidadAnfibios+=1
        Anfibio.salamandras+=1
        Anfibio._listado.append(self)

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


