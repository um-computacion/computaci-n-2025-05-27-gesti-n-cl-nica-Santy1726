class Turno:
    def __init__(self, fecha_hora, paciente, medico, motivo=""):
        self.fecha_hora = fecha_hora
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo

    def __str__(self):
        return (f"Turno: {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} - "
            f"Médico: {self.medico.obtener_nombre_completo()} - "
            f"Paciente: {self.paciente.obtener_nombre()} - "
            f"Motivo: {self.motivo}")



    
