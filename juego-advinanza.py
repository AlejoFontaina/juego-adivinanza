
import random 

numero_secreto = random.randint(0,100)
adivinado = False
cant_max_intentos = 10 
cant_intentos = 0
print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("Alcanzaste el maximo de intentos.")  
        break
    entrada = input ("Introducir numero que se encuentre entre 0 y 99: ")
    numero = int(entrada)
    cant_intentos += 1
    if numero == numero_secreto:
        print(f"Adivinaste el numero secreto! era el numero {numero_secreto}")
        adivinado = True
    elif numero < numero_secreto: 
        print("El numero ingresado es menor que el numero secreto")
    else: 
        print("El número ingresado es mayor que el numero secreto")