import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Ana", "12345678", "1990-01-01")
        self.medico = Medico("Laura", "Juárez", "22334455", "Clínica Médica", sexo="F")
        self.historia = HistoriaClinica(self.paciente)
        self.turno = Turno(datetime(2025, 6, 20, 10, 0), self.paciente, self.medico, "Chequeo general")
        self.receta = Receta(self.paciente, self.medico, ["Paracetamol", "Amoxicilina"])

    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertIs(turnos[0], self.turno)

    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIs(recetas[0], self.receta)

    def test_obtener_listas_devuelven_copias(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)

        turnos = self.historia.obtener_turnos()
        recetas = self.historia.obtener_recetas()

        turnos.append("otro turno")
        recetas.append("otra receta")

        self.assertEqual(len(self.historia.obtener_turnos()), 1)
        self.assertEqual(len(self.historia.obtener_recetas()), 1)

    def test_str_historia_clinica_con_datos(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        salida = str(self.historia)
        self.assertIn("Historia Clínica de Ana", salida)
        self.assertIn("Chequeo general", salida)
        self.assertIn("Paracetamol", salida)

    def test_str_historia_clinica_sin_datos(self):
        salida = str(self.historia)
        self.assertIn("No hay turnos registrados", salida)
        self.assertIn("No hay recetas registradas", salida)

if __name__ == "__main__":
    unittest.main()
