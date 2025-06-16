class Medico:
    def __init__(self, nombre, apellido, dni, especialidad, sexo="M"):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.especialidad = especialidad
        self.sexo = sexo      # "M" para masculino, "F" para femenino

    def obtener_dni(self):
        return self.dni

    def obtener_especialidad(self):
        return self.especialidad

    def obtener_nombre_completo(self):
        prefijo = "Dra." if self.sexo == "F" else "Dr."
        return f"{prefijo} {self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.obtener_nombre_completo()} (DNI: {self.dni}) - Especialidad: {self.especialidad}"

