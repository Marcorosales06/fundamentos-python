import random

z = random.randint(1,100)
x = 0



while x !=z:
    x = int(input("Ingresa un numero entre 1 y 100: "))
    if x < z:
        print("El numero secreto es mayor")

    elif  x > z:

        print("El numero secreto es menor")

print("Felicidades Has adivinado el numero secreto: ", z, "\nFin del juego")
