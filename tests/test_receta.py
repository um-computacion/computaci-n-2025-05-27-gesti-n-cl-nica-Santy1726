import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.receta import Receta

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan", "12345678", "01/01/2000")
        self.medico = Medico("Laura", "Juárez", "22334455", "Clínica Médica", sexo="F")
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_creacion_receta_correcta(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertEqual(receta._Receta__paciente, self.paciente)
        self.assertEqual(receta._Receta__medico, self.medico)
        self.assertEqual(receta._Receta__medicamentos, self.medicamentos)

    def test_receta_sin_medicamentos_lanza_error(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])

    def test_fecha_se_asigna_automaticamente(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        ahora = datetime.now()
        diferencia = ahora - receta._Receta__fecha
        self.assertLess(diferencia.total_seconds(), 5)

    def test_str_receta(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        salida = str(receta)
        self.assertIn("Juan", salida)
        self.assertIn("Dra. Laura Juárez", salida) 
        self.assertIn("Ibuprofeno", salida)

if __name__ == "__main__":
    unittest.main()
