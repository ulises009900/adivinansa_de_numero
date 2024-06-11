número=0
while intentosRealizados < 6:

    print('Intenta adivinar.') 

    estimación = input()

    estimación = int(estimación)



    intentosRealizados = intentosRealizados + 1


    if estimación < número:

        print('Tu numero es muy bajo .') 



    if estimación > número:

        print('Tu es muy alto.')



    if estimación == número:

        break


if estimación == número:

    intentosRealizados = str(intentosRealizados)

print("Has adivinado mi número en " + intentosRealizados )


if estimación != número:

    número = str(número)

print( "no. El número que estaba pensando era " + número)