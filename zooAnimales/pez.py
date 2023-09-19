from animal import Animal
class Pez(Animal):
    cantidadPeces=0
    salmones=0
    bacalaos=0
    _listado=[]

    def __init__(self,nombre, edad,habitad, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad,habitad, genero, colorEscamas, cantidadAletas)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez.cantidadPeces+=1
        Pez._listado.append(self)
    
    def crearSalmon(self,nombre,edad,genero):
        super().__init__(nombre,edad, "oceano", genero)
        self._colorEscamas="rojo"
        self._cantidadAletas=6
        Pez.salmones+=1
        Pez.cantidadPeces+=1
        Pez._listado.append(self)
    
    def crearBacalaos(self,nombre,edad,genero):
        super().__init__(nombre,edad, "oceano", genero)
        self._colorEscamas= "gris"
        self._cantidadAletas= 6
        Pez.bacalaos+=1
        Pez.cantidadPeces+=1
        Pez._listado.append(self)

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
    
    