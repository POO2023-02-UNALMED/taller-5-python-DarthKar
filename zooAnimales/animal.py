
class Animal:
    totalAnimales=0
    def __init__(self, nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat =habitat
        self._genero = genero
        self._zona = None

    
    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    @classmethod
    def totalPorTipo(self):
        from zooAnimales import Mamifero
        from zooAnimales import Ave
        from zooAnimales import Reptil
        from zooAnimales import Pez
        from zooAnimales import Anfibio
        "Mamiferos : "+ Mamifero.cantidadMamifero()+"\nAves : "+Ave.cantidadAves()+"\nReptiles : "+Reptil.cantidadReptiles()+"\nPeces : "+Pez.cantidadPeces()+"\nAnfibios : "+Anfibio.cantidadAnfibios()

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
    
    