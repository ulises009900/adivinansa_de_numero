import random
numero_secreto = random.randint(1, 100)
print("bienvenido al juego de a divinar el numero!")
print("Estoy pensando en un numero enter 1 y 100...")
print ("¿puedes adivinar cual es?")

eleccion=int(input("por favor ingrese el numero adivinar: "))
while (eleccion!=numero_secreto):
    if (eleccion >numero_secreto):
        eleccion=int(input("demasiado bajo. Intente ingresar un nuevo numero: "))
    else:
        eleccion=int(input("demasiado alto. Intente ingresar un nuevo numero: "))
        
        
        
print(eleccion, "FELICITACIONES! has adivinado el numero")
