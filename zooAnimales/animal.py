
class Animal:
    totalAnimales=0
    def __init__(self, nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat =habitat
        self._genero = genero
        self._zona = None

    
    def toString(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    @classmethod
    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        "Mamiferos : "+ Mamifero.cantidadMamiferos()+"\nAves : "+Ave.cantidadAves()+"\nReptiles : "+Reptil.cantidadReptiles()+"\nPeces : "+Pez.cantidadPeces()+"\nAnfibios : "+Anfibio.cantidadAnfibios()

    def movimiento(self):
        return "desplazarse"
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero
    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona = zona
    def getZona(self):
        return self._zona
    
    