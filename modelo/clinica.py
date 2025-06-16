from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException
)

class Clinica:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.medicos = []
        self.pacientes = []
        self.turnos = []
        self.especialidades = []
        self.__historias_clinicas = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_turno(self, turno):
        for t in self.turnos:
            if t.medico.dni == turno.medico.dni and t.fecha_hora == turno.fecha_hora:
                raise TurnoOcupadoException(
                    f"El médico ya tiene un turno el {turno.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
                )
        self.turnos.append(turno)

    def agregar_especialidad(self, especialidad):
        self.especialidades.append(especialidad)

    def agregar_historia_clinica(self, historia):
        self.__historias_clinicas.append(historia)

    def obtener_historia_clinica(self, dni_paciente):
        historia = next(
            (h for h in self.__historias_clinicas if h._HistoriaClinica__paciente.obtener_dni() == dni_paciente),
            None
        )
        if not historia:
            raise PacienteNoEncontradoException(f"No se encontró historia clínica para el paciente con DNI {dni_paciente}")
        return historia

    def buscar_medico_por_dni(self, dni):
        medico = next((m for m in self.medicos if m.dni == dni), None)
        if not medico:
            raise MedicoNoDisponibleException(f"No se encontró médico con DNI {dni}")
        return medico

    def buscar_paciente_por_dni(self, dni):
        paciente = next((p for p in self.pacientes if p.obtener_dni() == dni), None)
        if not paciente:
            raise PacienteNoEncontradoException(f"No se encontró paciente con DNI {dni}")
        return paciente

    def obtener_turnos_por_medico(self, dni_medico):
        return [t for t in self.turnos if t.medico.dni == dni_medico]

    def obtener_turnos_por_paciente(self, dni_paciente):
        return [t for t in self.turnos if t.paciente.obtener_dni() == dni_paciente]

    def __str__(self):
        return f"Clínica {self.nombre} con {len(self.medicos)} médicos, {len(self.pacientes)} pacientes y {len(self.turnos)} turnos"
