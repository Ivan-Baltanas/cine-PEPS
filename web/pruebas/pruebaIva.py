import sys
import os
import unittest

# Añade la ruta de la carpeta 'web' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from controlador_juegos import calculariva

class tests_calculariva(unittest.TestCase):
    def test_calculariva(self):
        self.assertEqual(calculariva(100), 21)

if __name__ == '__main__':
    unittest.main()
