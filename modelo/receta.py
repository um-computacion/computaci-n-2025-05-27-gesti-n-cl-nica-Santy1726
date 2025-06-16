from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        if not medicamentos:
            raise ValueError("La lista de medicamentos no puede estar vacía.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        return (
            f"Receta Médica\n"
            f"Paciente: {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()})\n"
            f"Medico: {self.__medico}\n"
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M')}\n"
            f"Medicamentos: {medicamentos_str}"
        )


