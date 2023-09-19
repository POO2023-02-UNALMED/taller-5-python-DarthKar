from zooAnimales.animal import Animal
class Reptil(Animal):
    canReptiles = 0
    iguanas=0
    serpientes=0
    _listado=[]
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.canReptiles +=1
        Reptil._listado.append(self)

    @classmethod
    def crearIguana(cls,nombre, edad,genero):
        iguana=cls(nombre, edad,"humedal", genero,"verde",3)
        Reptil.iguanas+=1
        return iguana

    @classmethod
    def crearSerpiente(cls,nombre, edad,genero):
        serpiente=cls(nombre, edad,"jungla",genero,"blanco",1)
        Reptil.serpientes+=1
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return cls.cantidadReptiles

    def movimiento(self):
        return "reptar" 

    def setListado(self,listado):
        self._listado=listado
    def getListado(self):
        return self._listado

    def setLargoCola(self,largo):
        self._largoCola = largo
    def getLargoCola(self):
        return self._largo
    
    def setColorEscamas(self,color):
        self._colorEscamas = color
    def getColorEscamas(self):
        return self._colorEscamas

