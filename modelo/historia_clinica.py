class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return self.__turnos.copy()

    def obtener_recetas(self):
        return self.__recetas.copy()

    def __str__(self):
        resultado = f"Historia Clínica de {self.__paciente.obtener_nombre()} (DNI: {self.__paciente.obtener_dni()})\n\n"
        resultado += "Turnos:\n"
        if self.__turnos:
            for turno in self.__turnos:
                resultado += f"- {turno}\n"
        else:
            resultado += "No hay turnos registrados.\n"

        resultado += "\nRecetas:\n"
        if self.__recetas:
            for receta in self.__recetas:
                resultado += f"- {receta}\n"
        else:
            resultado += "No hay recetas registradas.\n"

        return resultado
