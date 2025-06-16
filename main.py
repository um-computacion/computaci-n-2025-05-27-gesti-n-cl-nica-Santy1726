from modelo.clinica import Clinica
from interfaz.cli import CLI

def main():

    mi_clinica = Clinica("Santa Salud")

    cli = CLI(mi_clinica)

    cli.ejecutar()

if __name__ == "__main__":
    main()
