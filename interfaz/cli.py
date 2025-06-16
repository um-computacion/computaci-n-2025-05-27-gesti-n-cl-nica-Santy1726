from datetime import datetime
from modelo.medico import Medico
from modelo.paciente import Paciente
from modelo.historia_clinica import HistoriaClinica
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.especialidad import Especialidad
from modelo.excepciones import (
    MedicoNoDisponibleException,
    PacienteNoEncontradoException,
    TurnoOcupadoException,
    RecetaInvalidaException
)


class CLI:
    def __init__(self, clinica):
        self.clinica = clinica

    def mostrar_menu(self):
        print("\n--- Sistema de Gestión Clínica ---")
        print("1. Agregar médico")
        print("2. Agregar paciente")
        print("3. Agregar especialidad")
        print("4. Agregar turno")
        print("5. Agregar receta")
        print("6. Mostrar turnos")
        print("7. Mostrar historia clínica de un paciente")
        print("8. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_medico()
            elif opcion == "2":
                self.agregar_paciente()
            elif opcion == "3":
                self.agregar_especialidad()
            elif opcion == "4":
                self.agregar_turno()
            elif opcion == "5":
                self.agregar_receta()
            elif opcion == "6":
                self.mostrar_turnos()
            elif opcion == "7":
                self.mostrar_historia_clinica()
            elif opcion == "8":
                print("Gracias por usar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida, intente de nuevo.")

    def agregar_medico(self):
        try:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            especialidad_nombre = input("Especialidad: ")
            sexo = input("Sexo (M/F): ").upper()
            if sexo not in ["M", "F"]:
                sexo = "M"
                
            especialidad = next((e for e in self.clinica.especialidades if e.obtener_nombre() == especialidad_nombre), None)
            if not especialidad:
                print(f"No existe la especialidad '{especialidad_nombre}'. Debe crearla primero.")
                return

            medico = Medico(nombre, apellido, dni, especialidad, sexo)
            self.clinica.agregar_medico(medico)
            print(f"Médico agregado: {medico}")
        except Exception as e:
            print(f"Error al agregar médico: {e}")

    def agregar_paciente(self):
        try:
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            fecha_nac = input("Fecha de nacimiento (DD/MM/AAAA): ")
            paciente = Paciente(nombre, dni, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            # Crear historia clínica automáticamente
            historia = HistoriaClinica(paciente)
            self.clinica.agregar_historia_clinica(historia)
            print(f"Paciente agregado: {paciente}")
        except Exception as e:
            print(f"Error al agregar paciente: {e}")

    def agregar_especialidad(self):
        try:
            nombre = input("Nombre de la especialidad: ")
            descripcion = input("Descripción: ")
            especialidad = Especialidad(nombre, descripcion)
            self.clinica.agregar_especialidad(especialidad)
            print(f"Especialidad agregada: {especialidad}")
        except Exception as e:
            print(f"Error al agregar especialidad: {e}")

    def agregar_turno(self):
        try:
            dni_medico = input("DNI del médico: ")
            medico = self.clinica.buscar_medico_por_dni(dni_medico)

            dni_paciente = input("DNI del paciente: ")
            paciente = self.clinica.buscar_paciente_por_dni(dni_paciente)

            fecha_str = input("Fecha y hora del turno (DD/MM/AAAA HH:MM): ")
            fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")

            motivo = input("Motivo (opcional): ")

            turno = Turno(fecha_hora, paciente, medico, motivo)
            self.clinica.agregar_turno(turno)

            historia = self.clinica.obtener_historia_clinica(dni_paciente)
            historia.agregar_turno(turno)

            print(f"Turno agregado: {turno}")

        except MedicoNoDisponibleException as e:
            print(f"Error: {e}")
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")
        except TurnoOcupadoException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Formato de fecha inválido. Use DD/MM/AAAA HH:MM.")
        except Exception as e:
            print(f"Error inesperado al agregar turno: {e}")

    def agregar_receta(self):
        try:
            dni_medico = input("DNI del médico: ")
            medico = self.clinica.buscar_medico_por_dni(dni_medico)

            dni_paciente = input("DNI del paciente: ")
            paciente = self.clinica.buscar_paciente_por_dni(dni_paciente)

            medicamentos_str = input("Medicamentos (separados por coma): ")
            medicamentos = [m.strip() for m in medicamentos_str.split(",") if m.strip()]
            if not medicamentos:
                raise RecetaInvalidaException("Debe ingresar al menos un medicamento.")

            receta = Receta(paciente, medico.obtener_nombre_completo(), medicamentos)

            historia = self.clinica.obtener_historia_clinica(dni_paciente)
            historia.agregar_receta(receta)

            print("Receta agregada:")
            print(receta)

        except MedicoNoDisponibleException as e:
            print(f"Error: {e}")
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")
        except RecetaInvalidaException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado al agregar receta: {e}")

    def mostrar_turnos(self):
        turnos = self.clinica.mostrar_turnos()
        if turnos:
            print("\nTurnos registrados:")
            for t in turnos:
                print(t)
        else:
            print("No hay turnos registrados.")

    def mostrar_historia_clinica(self):
        try:
            dni = input("Ingrese DNI del paciente: ")
            historia = self.clinica.obtener_historia_clinica(dni)
            print("\n" + str(historia))
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")

