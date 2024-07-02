import logging
import random


logging.basicConfig(nombre_archivo='game.log', nivel=logging.INFO,
                    format='%(activo)s - %(nombre_nivel)s - %(mensaje)s')

def inisiando_juego():
    logging.info("El juego ha comenzado.")
    numeros_random = random.randint(1, 100)
    intentos = 0
    adivinada = False

    logging.info(f"El número a adivinar ha sido generado: {numeros_random}")

    while not adivinada:
        try:
            guess = int(input("Adivina el número entre 1 y 100: "))
            intentos += 1
            logging.info(f"Intento {intentos}: el jugador adivinó {guess}")

            if guess < numeros_random:
                print("Más alto...")
                logging.info("El jugador adivinó demasiado bajo.")
            elif guess > numeros_random:
                print("Más bajo...")
                logging.info("El jugador adivinó demasiado alto.")
            else:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                logging.info(f"El jugador adivinó correctamente en {intentos} intentos.")
                adivinada = True
        except ValueError:
            print("Por favor, introduce un número válido.")
            logging.error("El jugador introdujo un valor no válido.")

if __name__ == "__main__":
    inisiando_juego()








