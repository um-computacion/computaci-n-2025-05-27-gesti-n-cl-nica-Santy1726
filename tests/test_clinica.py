import unittest
from modelo.clinica import Clinica
from modelo.medico import Medico
from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.especialidad import Especialidad
from datetime import datetime

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica("Clinica General")

        self.especialidad = Especialidad("Cardiología", "Tratamiento del corazón")
        self.medico = Medico("Juan", "Pérez", "40526387", self.especialidad)
        self.paciente = Paciente("Carlos Pérez", "29654321", "01/01/1980")
        self.turno = Turno(datetime(2025, 6, 15, 10, 0), self.paciente, self.medico)

        self.clinica.agregar_medico(self.medico)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_turno(self.turno)

    def test_buscar_medico_por_dni(self):
        encontrado = self.clinica.buscar_medico_por_dni("40526387")
        self.assertEqual(encontrado, self.medico)

    def test_buscar_paciente_por_dni(self):
        encontrado = self.clinica.buscar_paciente_por_dni("29654321")
        self.assertEqual(encontrado, self.paciente)

    def test_mostrar_turnos(self):
        turnos = self.clinica.mostrar_turnos()
        # Ahora buscamos el string completo que genera __str__ del turno:
        esperado = "Turno: 15/06/2025 10:00 - Médico: Dr. Juan Pérez - Paciente: Carlos Pérez"
        self.assertIn(esperado, turnos)

if __name__ == '__main__':
    unittest.main()
