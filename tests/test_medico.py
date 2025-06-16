import unittest
from modelo.medico import Medico

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico("Juan", "Perez", "25478693", "Cardiología")

    def test_creacion_medico(self):
        self.assertEqual(self.medico.nombre, "Juan")
        self.assertEqual(self.medico.apellido, "Perez")
        self.assertEqual(self.medico.dni, "25478693")
        self.assertEqual(self.medico.especialidad, "Cardiología")

    def test_obtener_especialidad_para_dia(self):
        self.assertEqual(self.medico.obtener_especialidad(), "Cardiología")

    def test_str_medico(self):
        esperado = "Dr. Juan Perez (DNI: 25478693) - Especialidad: Cardiología"
        self.assertEqual(str(self.medico), esperado)

    def test_obtener_dni(self):
        self.assertEqual(self.medico.obtener_dni(), "25478693")

    def test_str_con_dni_incorrecto(self):
        medico_incorrecto = Medico("Ana", "Gómez", "87654321", "Pediatría")
        esperado = "Dr. Ana Gómez (DNI: 87654321) - Especialidad: Pediatría"
        self.assertEqual(str(medico_incorrecto), esperado)
    
    def test_str_con_especialidad_incorrecta(self):
        medico_incorrecto = Medico("Carlos", "López", "12345678", "Dermatología")
        esperado = "Dr. Carlos López (DNI: 12345678) - Especialidad: Dermatología"
        self.assertEqual(str(medico_incorrecto), esperado)