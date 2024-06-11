import random
numero_secreto = random.randint(1, 100)

eleccion=int(input("adivine el numero: "))
while (eleccion!=numero_secreto):
    if (eleccion >numero_secreto):
        eleccion=int(input("menos: "))
    else:
        eleccion=int(input("mas: "))
        
        
        
print(eleccion, " es correcto")