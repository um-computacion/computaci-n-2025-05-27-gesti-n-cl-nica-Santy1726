import unittest
from modelo.excepciones import (
    MedicoNoDisponibleException,
    PacienteNoEncontradoException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestExcepciones(unittest.TestCase):

    def test_medico_no_disponible_exception(self):
        mensaje = "No hay médicos disponibles en esta especialidad."
        with self.assertRaises(MedicoNoDisponibleException) as contexto:
            raise MedicoNoDisponibleException(mensaje)
        self.assertEqual(str(contexto.exception), mensaje)

    def test_paciente_no_encontrado_exception(self):
        mensaje = "El paciente con DNI 123 no fue encontrado."
        with self.assertRaises(PacienteNoEncontradoException) as contexto:
            raise PacienteNoEncontradoException(mensaje)
        self.assertEqual(str(contexto.exception), mensaje)

    def test_turno_ocupado_exception(self):
        mensaje = "El turno ya está ocupado para ese horario."
        with self.assertRaises(TurnoOcupadoException) as contexto:
            raise TurnoOcupadoException(mensaje)
        self.assertEqual(str(contexto.exception), mensaje)

    def test_receta_invalida_exception(self):
        mensaje = "Debe ingresar al menos un medicamento."
        with self.assertRaises(RecetaInvalidaException) as contexto:
            raise RecetaInvalidaException(mensaje)
        self.assertEqual(str(contexto.exception), mensaje)

if __name__ == '__main__':
    unittest.main()
