import tkinter as tk
from num2words import num2words

# Crear una ventana
ventana = tk.Tk()

# Configurar propiedades de la ventana
ventana.title("Mi Aplicación")
ventana.geometry("280x400")

# Función que se ejecuta al hacer clic en el botón
def escribir_numero():
    numero = entrada.get()
    if numero.isnumeric():
        texto = num2words(numero, lang="es")
        mensaje = "El numero es: " + texto + "!"
       
    else:
        mensaje = "No es valido lo recibido en el input"
    etiqueta_numero_escrito.config(text=mensaje)

# Crear una etiqueta
etiqueta_numero = tk.Label(ventana, text="Ingresa el numero que quieres escribir:", bg='#4F709C', height=3, font=3, fg='#F5EFE7', width=30)
etiqueta_numero.grid(row=0, column=0, columnspan=2)
# Crear una entrada de texto
entrada = tk.Entry(ventana,  width=30)

# Crear un botón
boton_escribir = tk.Button(ventana, text="Escribir", command=escribir_numero, width=30)

# Colocar los elementos en la cuadrícula
entrada.grid(row=1, column=0, padx=5, pady=5)
boton_escribir.grid(row=2, column=0, padx=5, pady=5)

# Crear una etiqueta para mostrar el saludo
etiqueta_numero_escrito = tk.Label(ventana, text="")
etiqueta_numero_escrito.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle de eventos de la aplicación
ventana.mainloop()