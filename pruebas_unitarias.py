import logging
import random

# Configuración del logging
logging.basicConfig(filename='adivinanza_numero.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generar_numero():
    return random.randint(1, 100)

def revisar_numero(numero_a_adivinar, numero):
    if numero < numero_a_adivinar:
        return "mas alto"
    elif numero > numero_a_adivinar:
        return "mas bajo"
    else:
        return "correcto"

def empezar_juego():
    logging.info("El juego ha comenzado.")
    numero_a_adivinar = generar_numero()
    intentos = 0
    adivinado = False

    logging.info(f"El número a adivinar ha sido generado: {numero_a_adivinar}")

    while not adivinado:
        try:
            numero = int(input("Adivina el número entre 1 y 100: "))
            intentos += 1
            logging.info(f"Intento {intentos}: el jugador adivinó {numero}")

            resultado = revisar_numero(numero_a_adivinar, numero)
            if resultado == "mas alto":
                print("Más alto...")
                logging.info("El jugador adivinó demasiado bajo.")
            elif resultado == "mas bajo":
                print("Más bajo...")
                logging.info("El jugador adivinó demasiado alto.")
            else:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                logging.info(f"El jugador adivinó correctamente en {intentos} intentos.")
                adivinado = True
        except ValueError:
            print("Por favor, introduce un número válido.")
            logging.error("El jugador introdujo un valor no válido.")

if __name__ == "__main__":
    empezar_juego()
