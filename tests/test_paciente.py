import unittest
from modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "28345964", "01/01/1990")

    def test_obtener_dni(self):
        self.assertEqual(self.paciente.obtener_dni(), "28345964")

    def test_str(self):
        esperado = "Paciente: Juan Pérez (DNI: 28345964, Fecha de nacimiento: 01/01/1990)"
        self.assertEqual(str(self.paciente), esperado)

    def test_str_con_dni_incorrecto(self):
        paciente_incorrecto = Paciente("Ana Gómez", "48769321", "02/02/1992")
        esperado = "Paciente: Ana Gómez (DNI: 48769321, Fecha de nacimiento: 02/02/1992)"
        self.assertEqual(str(paciente_incorrecto), esperado)

    def test_str_con_fecha_nacimiento_incorrecta(self):
        paciente_incorrecto = Paciente("Carlos López", "12345678", "31/12/1985")
        esperado = "Paciente: Carlos López (DNI: 12345678, Fecha de nacimiento: 31/12/1985)"
        self.assertEqual(str(paciente_incorrecto), esperado)
    
    def test_str_con_nombre_incorrecto(self):
        paciente_incorrecto = Paciente("María", "98765432", "15/03/1988")
        esperado = "Paciente: María (DNI: 98765432, Fecha de nacimiento: 15/03/1988)"
        self.assertEqual(str(paciente_incorrecto), esperado)    

if __name__ == '__main__':
    unittest.main()
