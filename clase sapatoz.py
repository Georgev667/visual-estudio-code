class zapatos:
    def __init__(self, estilo, color, talla, marca):
        self.estilo = estilo
        self.color = color
        self.talla = talla
        self.marca = marca

    def mostrar_disponibilidad(self, cantidad):
        if cantidad > 0:
            return f"El zapato {self.estilo} de color {self.color} está disponible en talla {self.talla} y marca {self.marca}."
        else:
            return f"El zapato {self.estilo} de color {self.color} no está disponible en talla {self.talla} y marca {self.marca}."

            