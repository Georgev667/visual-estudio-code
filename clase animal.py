class animal:
    def __init__(self, especie, nombre,color):
        self.nombre = nombre
        self.especie = especie
        self.color = color
    def hacersonido(self):
        return (f"Este animal hace un sonido")
    def presentarse(self):
        return (f"Hola, soy un {self.especie} y me llamo {self.nombre} y soy de color {self.color}")   

class perro(animal):
    def __init__(self, especie, nombre,color,raza):
        super().__init__(especie, nombre,color)
        self.raza = raza
    def hacersonido(self):
        return (f"Guau Guau")
    def presentarse(self):
        return (f"Hola, soy un {self.especie} y me llamo {self.nombre} y soy de color {self.color} y mi raza es {self.raza}")
    def buscarpelota(self):
        return (f"({self.nombre} está buscando la pelota)")

class gato(animal):
    def __init__(self, especie, nombre,color,raza):
        super().__init__(especie, nombre,color)
        self.raza = raza
    def hacersonido(self):
        return (f"Miau Miau")
    def presentarse(self):
        return (f"Hola, soy un {self.especie} y me llamo {self.nombre} y soy de color {self.color} y mi raza es {self.raza}")
    def trepararbol(self):
        return (f"({self.nombre} está trepando un árbol)")





class   pajaro(animal):
    def __init__(self, especie, nombre,color,raza):
        super().__init__(especie, nombre,color)
        self.raza = raza
    def hacersonido(self):
        return (f"pio pio")
    def presentarse(self):
        return (f"Hola, soy un {self.especie} y me llamo {self.nombre} y soy de color {self.color} y mi raza es {self.raza}")
    def volar(self):
        return (f"({self.nombre} está volando)")