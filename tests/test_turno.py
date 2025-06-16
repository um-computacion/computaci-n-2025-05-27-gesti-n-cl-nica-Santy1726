import unittest
from datetime import datetime
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        especialidad = Especialidad("Cardiología", "Estudio y tratamiento del corazón")
        self.medico = Medico("Juan", "López", "87654321", especialidad)
        self.fecha = datetime(2025, 6, 14, 15, 30)
        self.turno = Turno(self.fecha, self.paciente, self.medico, "Consulta general")

    def test_str(self):
        esperado = "Turno: 14/06/2025 15:30 - Médico: Dr. Juan López - Paciente: Juan Perez"
        self.assertEqual(str(self.turno), esperado)

if __name__ == "__main__":
    unittest.main()
()

