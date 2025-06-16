import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def setUp(self):
        self.especialidad = Especialidad("Cardiología", "Estudio y tratamiento del corazón")

    def test_creacion_especialidad(self):
        self.assertEqual(self.especialidad.nombre, "Cardiología")
        self.assertEqual(self.especialidad.descripcion, "Estudio y tratamiento del corazón")

    def test_modificar_nombre(self):
        self.especialidad.nombre = "Neurología"
        self.assertEqual(self.especialidad.nombre, "Neurología")

    def test_modificar_descripcion(self):
        self.especialidad.descripcion = "Estudio del sistema nervioso"
        self.assertEqual(self.especialidad.descripcion, "Estudio del sistema nervioso")

    def test_str_especialidad(self):
        esperado = "Especialidad: Cardiología - Estudio y tratamiento del corazón"
        self.assertEqual(str(self.especialidad), esperado)

    def test_str_pediatria(self):
        especialidad = Especialidad("Pediatría", "Atención médica infantil")
        esperado = "Especialidad: Pediatría - Atención médica infantil"
        self.assertEqual(str(especialidad), esperado)

    def test_str_Dematologia(self):
        especialidad = Especialidad("Dermatología", "Tratamiento de enfermedades de la piel")
        esperado = "Especialidad: Dermatología - Tratamiento de enfermedades de la piel"
        self.assertEqual(str(especialidad), esperado)        

if __name__ == "__main__":
    unittest.main()

