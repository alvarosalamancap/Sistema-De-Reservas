class Reserva:
    def __init__(self, fecha, hora, nombre_cliente, cantidad_personas):
        self.fecha = fecha
        self.hora = hora
        self.nombre_cliente = nombre_cliente
        self.cantidad_personas = cantidad_personas

class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def hacer_reserva(self, reserva):
        self.reservas.append(reserva)
        print("Reserva realizada con éxito!")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas realizadas.")
        else:
            print("Reservas:")
            for i, reserva in enumerate(self.reservas, 1):
                print(f"{i}. Fecha: {reserva.fecha}, Hora: {reserva.hora}, Cliente: {reserva.nombre_cliente}, Personas: {reserva.cantidad_personas}")

def mostrar_menu_bienvenida():
    print("************************************")
    print("    Bienvenido a Hotels ALVARO STARS by @alvarosalamancap  ")
    print("************************************")
    print("1. Hacer reserva")
    print("2. Mostrar reservas")
    print("3. Salir")

def main():
    sistema_reservas = SistemaReservas()

    while True:
        mostrar_menu_bienvenida()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fecha = input("Ingrese la fecha de la reserva (DD/MM/AAAA): ")
            hora = input("Ingrese la hora de la reserva: ")
            nombre_cliente = input("Ingrese su nombre: ")
            cantidad_personas = int(input("Ingrese la cantidad de personas: "))
            reserva = Reserva(fecha, hora, nombre_cliente, cantidad_personas)
            sistema_reservas.hacer_reserva(reserva)
        elif opcion == "2":
            sistema_reservas.mostrar_reservas()
        elif opcion == "3":
            print("Saliendo del sistema de reservas en Hotels Alvaro Star. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
