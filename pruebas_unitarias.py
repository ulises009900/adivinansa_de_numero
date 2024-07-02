import unittest
from logica_2 import revisar_numero, generar_numero

class TestGuessingGame(unittest.TestCase):

    def test_revisar_numero_correct(self):
        self.assertEqual(revisar_numero(50, 50), "correcto")

    def test_revisar_numero_higher(self):
        self.assertEqual(revisar_numero(50, 40), "mas alto")

    def test_revisar_numero_lower(self):
        self.assertEqual(revisar_numero(50, 60), "mas bajo")

    def test_generar_numero_range(self):
        for _ in range(1000):
            numero = generar_numero()
            self.assertTrue(1 <= numero <= 100, f"Número generado fuera de rango: {numero}")

if __name__ == '__main__':
    unittest.main(verbosity=2)

if estimación != número:

    número = str(número)

print( "no. El número que estaba pensando era " + número)
