class Zoologico:

    def __init__(self,nombre,ubicacion):
        
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas=[]

    def agregarZonas(self,zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        total=0
        for i in range(len(self._zonas)):
           total+=len(self._zonas[i])
        return total
    
    def setNombre(self,nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion
    def getUbicacion(self):
        return self._ubicacion
    
    def setZona(self,zonas):
        self._zonas = zonas
    def getZona(self,num):
        return self._zonas[num]
    
    