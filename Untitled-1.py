cantidad_salones = int(input("Ingrese la cantidad de salones: "))
contador_salones = 1
while contador_salones <= cantidad_salones:
    cantidad_estudiantes = int(input(f"Ingrese la cantidad de estudiantes en el salón {contador_salones}: "))
    suma_edades = 0
    contador_estudiantes = 1
    while contador_estudiantes <= cantidad_estudiantes:
        edad_estudiante = float(input(f"Ingrese la edad del estudiante {contador_estudiantes} en el salón {contador_salones}: "))
        suma_edades += edad_estudiante
        contador_estudiantes += 1
    promedio_edad = suma_edades / cantidad_estudiantes
    print(f"El promedio de edad en el salón {contador_salones} es: {promedio_edad:.2f}")
    contador_salones += 1
    