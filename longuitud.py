import math
x1 = float(input("ingrese x1: "))
y1 = float(input("ingrese y1: "))
x2 = float(input("ingrese x2: "))
y2 = float(input("ingrese y2: "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los puntos es: {distancia}")