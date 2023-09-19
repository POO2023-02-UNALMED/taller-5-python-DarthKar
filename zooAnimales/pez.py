from zooAnimales.animal import Animal
class Pez(Animal):
    canPeces=0
    salmones=0
    bacalaos=0
    _listado=[]

    def __init__(self,nombre, edad,habitad, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad,habitad, genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez.canPeces+=1
        Pez._listado.append(self)
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        salmon = cls(nombre,edad, "oceano", genero,"rojo",6)
        Pez.salmones+=1
        return salmon
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        bacalao=cls(nombre,edad, "oceano", genero,"gris",6)
        Pez.bacalaos+=1
        return bacalao

    @classmethod
    def cantidadPez(cls):
        return cls.cantidadPeces

    def movimiento(self):
        return "nadar"

    def setListado(self,listado):
        self._listado=listado
    def getListado(self):
        return self._listado
    
    def setColorEscamas(self, color):
        self._colorEscamas=color
    def getColorEscamas(self):
        return self._colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas=cantidadAletas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    