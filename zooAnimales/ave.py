from zooAnimales.animal import Animal
class Ave(Animal):
    canAves=0
    halcones=0
    aguilas=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas= colorPlumas
        Ave.canAves+=1
        Ave._listado.append(self)

    @classmethod
    def crearAguila(cls,nombre,edad,genero): 
        aguila = cls(nombre, edad,"montanas", genero, "blanco y amarillo")
        Ave.aguilas+=1
        return aguila
    
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon = cls(nombre, edad,"montanas",genero,"cafe glorioso")
        Ave.halcones+=1
        return halcon
    
    @classmethod
    def cantidadAves(cls):
        return cls.cantidadAves
    
    def movimiento(self):
        return "volar"
    
    def setListado(self,listado):
        self._listado = listado
    def getListado(self):
        return self._listado
    
    def setColorPlumas(self,colorPLumas):
        self._colorPlumas = colorPLumas
    def getColorPlumas(self):
        return self._colorPlumas