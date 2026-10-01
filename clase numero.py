class Numeros:
    def __init__(self):
        self.numeros = []

    def agregar_numero(self, numero):
        self.numeros.append(numero)

    def mostrar_mayor(self):
        return max(self.numeros)

    def mostrar_menor(self):
        return min(self.numeros)

    def calcular_promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def ordenar_mayor_menor(self):
        return sorted(self.numeros, reverse=True)

    def ordenar_menor_mayor(self):
        return sorted(self.numeros)


lista = Numeros()

cantidad = int(input("¿Cuántos números quieres ingresar? "))

for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    lista.agregar_numero(numero)


while True:
    print("\n===== MENÚ =====")
    print("1. Ver número mayor")
    print("2. Ver número menor")
    print("3. Ver promedio")
    print("4. Ordenar de mayor a menor")
    print("5. Ordenar de menor a mayor")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("El número mayor es:", lista.mostrar_mayor())

    elif opcion == "2":
        print("El número menor es:", lista.mostrar_menor())

    elif opcion == "3":
        print("El promedio es:", lista.calcular_promedio())

    elif opcion == "4":
        print("De mayor a menor:", lista.ordenar_mayor_menor())

    elif opcion == "5":
        print("De menor a mayor:", lista.ordenar_menor_mayor())

    elif opcion == "6":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")