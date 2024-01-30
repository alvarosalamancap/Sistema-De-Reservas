import tkinter as tk
from tkinter import ttk, messagebox

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
        messagebox.showinfo("Éxito", "Reserva realizada con éxito!")

    def mostrar_reservas(self):
        if not self.reservas:
            messagebox.showinfo("Info", "No hay reservas realizadas.")
        else:
            reservas_info = "\n".join([f"Fecha: {reserva.fecha}, Hora: {reserva.hora}, Cliente: {reserva.nombre_cliente}, Personas: {reserva.cantidad_personas}" for reserva in self.reservas])
            messagebox.showinfo("Reservas", reservas_info)

class SistemaReservasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotels Alvaro Star - Sistema de Reservas")

        # Estilo moderno con colores azules
        style = ttk.Style()
        style.configure("TFrame", background="#3498db")
        style.configure("TLabel", background="#3498db", foreground="white", font=("Helvetica", 12))
        style.configure("TButton", background="#3498db", foreground="#001f3f", font=("Helvetica", 12))
        style.configure("TEntry", font=("Helvetica", 12))

        self.sistema_reservas = SistemaReservas()

        self.menu_bienvenida()

    def menu_bienvenida(self):
        frame_bienvenida = ttk.Frame(self.root, padding="20")
        frame_bienvenida.grid(row=0, column=0, sticky="nsew")

        label_bienvenida = ttk.Label(frame_bienvenida, text="¡Bienvenido a Hotels Alvaro Star!", font=("Helvetica", 16))
        label_bienvenida.grid(row=0, column=0, columnspan=2, pady=20)

        boton_reserva = ttk.Button(frame_bienvenida, text="Hacer Reserva", command=self.mostrar_formulario_reserva)
        boton_reserva.grid(row=1, column=0, pady=10)

        boton_mostrar_reservas = ttk.Button(frame_bienvenida, text="Mostrar Reservas", command=self.mostrar_reservas)
        boton_mostrar_reservas.grid(row=1, column=1, pady=10)

        boton_salir = ttk.Button(frame_bienvenida, text="Salir", command=self.root.destroy)
        boton_salir.grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_formulario_reserva(self):
        formulario_reserva = tk.Toplevel(self.root)
        formulario_reserva.title("Formulario de Reserva")

        label_fecha = ttk.Label(formulario_reserva, text="Fecha:")
        label_fecha.grid(row=0, column=0, padx=10, pady=10)
        entry_fecha = ttk.Entry(formulario_reserva)
        entry_fecha.grid(row=0, column=1, padx=10, pady=10)

        label_hora = ttk.Label(formulario_reserva, text="Hora:")
        label_hora.grid(row=1, column=0, padx=10, pady=10)
        entry_hora = ttk.Entry(formulario_reserva)
        entry_hora.grid(row=1, column=1, padx=10, pady=10)

        label_cliente = ttk.Label(formulario_reserva, text="Nombre del Cliente:")
        label_cliente.grid(row=2, column=0, padx=10, pady=10)
        entry_cliente = ttk.Entry(formulario_reserva)
        entry_cliente.grid(row=2, column=1, padx=10, pady=10)

        label_personas = ttk.Label(formulario_reserva, text="Cantidad de Personas:")
        label_personas.grid(row=3, column=0, padx=10, pady=10)
        entry_personas = ttk.Entry(formulario_reserva)
        entry_personas.grid(row=3, column=1, padx=10, pady=10)

        boton_confirmar = ttk.Button(formulario_reserva, text="Confirmar Reserva", command=lambda: self.confirmar_reserva(
            entry_fecha.get(), entry_hora.get(), entry_cliente.get(), entry_personas.get(), formulario_reserva))
        boton_confirmar.grid(row=4, column=0, columnspan=2, pady=20)

    def confirmar_reserva(self, fecha, hora, cliente, personas, ventana_padre):
        try:
            cantidad_personas = int(personas)
            reserva = Reserva(fecha, hora, cliente, cantidad_personas)
            self.sistema_reservas.hacer_reserva(reserva)
            ventana_padre.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido para la cantidad de personas.")

    def mostrar_reservas(self):
        self.sistema_reservas.mostrar_reservas()

def main():
    root = tk.Tk()
    app = SistemaReservasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
