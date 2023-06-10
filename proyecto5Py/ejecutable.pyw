import tkinter as tk

def agregar_numero(numero):
    global numero_marcado
    numero_marcado += str(numero)
    pantalla.config(text=numero_marcado)

def borrar_ultimo_numero():
    global numero_marcado
    numero_marcado = numero_marcado[:-1]
    pantalla.config(text=numero_marcado)

def realizar_llamada():
    # Aquí puedes agregar la lógica para realizar la llamada telefónica
    pantalla.config(text=f"llamando a {numero_marcado}...")
    print("Llamando al número:", numero_marcado)

ventana = tk.Tk()
ventana.title("Marcador Telefónico")
ventana.configure(bg="#ebebeb")

numero_marcado = ""
pantalla = tk.Label(ventana, text="", font=("Arial", 20), bg="white", fg="black", width=15, height=2)
pantalla.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Estilo para los botones del teclado numérico
boton_estilo = {
    "font": ("Arial", 16),
    "width": 5,
    "height": 2,
    "relief": "raised",
    "bg": "#ededed",
    "fg": "black",
}

# Crear los botones del teclado numérico
boton1 = tk.Button(ventana, text="1", command=lambda: agregar_numero(1), **boton_estilo)
boton1.grid(row=1, column=0, padx=5, pady=5)
boton2 = tk.Button(ventana, text="2", command=lambda: agregar_numero(2), **boton_estilo)
boton2.grid(row=1, column=1, padx=5, pady=5)
boton3 = tk.Button(ventana, text="3", command=lambda: agregar_numero(3), **boton_estilo)
boton3.grid(row=1, column=2, padx=5, pady=5)
boton4 = tk.Button(ventana, text="4", command=lambda: agregar_numero(4), **boton_estilo)
boton4.grid(row=2, column=0, padx=5, pady=5)
boton5 = tk.Button(ventana, text="5", command=lambda: agregar_numero(5), **boton_estilo)
boton5.grid(row=2, column=1, padx=5, pady=5)
boton6 = tk.Button(ventana, text="6", command=lambda: agregar_numero(6), **boton_estilo)
boton6.grid(row=2, column=2, padx=5, pady=5)
boton7 = tk.Button(ventana, text="7", command=lambda: agregar_numero(7), **boton_estilo)
boton7.grid(row=3, column=0, padx=5, pady=5)
boton8 = tk.Button(ventana, text="8", command=lambda: agregar_numero(8), **boton_estilo)
boton8.grid(row=3, column=1, padx=5, pady=5)
boton9 = tk.Button(ventana, text="9", command=lambda: agregar_numero(9), **boton_estilo)
boton9.grid(row=3, column=2, padx=5, pady=5)
boton0 = tk.Button(ventana, text="0", command=lambda: agregar_numero(0), **boton_estilo)
boton0.grid(row=4, column=1, padx=5, pady=5)

# Botón de borrar último número
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_ultimo_numero, **boton_estilo)
boton_borrar.grid(row=4, column=0, padx=5, pady=5)

# Botón de realizar llamada
boton_llamar = tk.Button(ventana, text="Llamar", command=realizar_llamada, **boton_estilo)
boton_llamar.grid(row=4, column=2, padx=5, pady=5)

ventana.mainloop()
