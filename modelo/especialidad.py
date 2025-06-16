class Especialidad:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def obtener_nombre(self):
        return self.nombre

    def obtener_descripcion(self):
        return self.descripcion

    def __str__(self):
        return f"Especialidad: {self.nombre} - {self.descripcion}"
