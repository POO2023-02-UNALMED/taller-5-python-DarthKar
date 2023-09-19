from zooAnimales.animal import Animal
class Ave(Animal):
    cantidadAves=0
    halcones=0
    aguilas=0
    _listado=[]

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas= colorPlumas
        Ave.cantidadAves+=1
        Ave._listado.append(self)

    def crearAguilas(self,nombre,edad,genero): 
        super().__init__(nombre, edad,"montanas", genero)
        self._colorPlumas = "blanco y amarillo"
        Ave.cantidadAves+=1
        Ave.Aguilas+=1
        Ave._listado.append(self)
    
    def crearHalcon(self,nombre,edad,genero):
        super().__init__(nombre, edad,"montanas",genero)
        self._colorPlumas = "cafe glorioso"
        Ave.cantidadAves+=1
        Ave.Halcones+=1
        Ave._listado.append(self)   
    
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