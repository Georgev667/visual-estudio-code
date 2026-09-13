
import random
min=1
max=100
numero_secreto = random.randint(min, max)
intento = 0
adivino = False
while intento <6 and not adivino:
    print(f"\nintento {intento + 1} de 6")
    numero_usuario = int(input("ingresa un numero entre 1 y 100: "))
    intento +=1
    if numero_usuario == numero_secreto:
            print("!secreto!")
            adivino = True
    elif numero_usuario > numero_secreto:
        print("el numero secreto es menor")
    else:
        print("el numero secreto es mayor")
if not adivino:
    print(f"\nnumero secreto era {numero_secreto}")