from zooAnimales.animal import Animal
class Reptil(Animal):
    cantidadReptiles = 0
    iguanas=0
    serpientes=0
    _listado=[]
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.cantidadReptiles +=1
        Reptil._listado.append(self)

    def crearIguana(self,nombre, edad,genero):
        super().__init__(nombre, edad,"humedal", genero)
        self._colorEscamas="verde"
        self._largoCola=3
        Reptil.cantidadReptiles+=1
        Reptil.iguanas+=1
        Reptil._listado.append(self)

    def crearSerpientes(self,nombre, edad,genero):
        super().__init__(nombre, edad,"jungla",genero)
        self._colorEscamas="blanco"
        self._largoCola=1
        Reptil.cantidadReptiles+=1
        Reptil.serpientes+=1
        Reptil._listado.append(self)     

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

