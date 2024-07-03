import logging
import random

# Configuración del logging
logging.basicConfig(filename='game.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def iniciando_juego():
    logging.info("El juego ha comenzado.")
    numero_random = random.randint(1, 100)
    intentos = 0
    adivinada = False

    logging.info(f"El número a adivinar ha sido generado: {numero_random}")

    while not adivinada:
        try:
            guess = int(input("Adivina el número entre 1 y 100: "))
            intentos += 1
            logging.info(f"Intento {intentos}: el jugador adivinó {guess}")

            if guess < numero_random:
                print("Más alto...")
                logging.info("El jugador adivinó demasiado bajo.")
            elif guess > numero_random:
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
    iniciando_juego()




