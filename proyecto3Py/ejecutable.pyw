import tkinter as tk
from apicalls import buscar_titulo, buscar_rating

# Crear ventanta
ventana = tk.Tk()

ventana.title('Rating de peliculas')
ventana.geometry("600x400")

# Funcion al hacer click al boton
def buscar_el_rating():
    nombre_pelicula = entrada.get()
    ids_peliculas = buscar_titulo(nombre_pelicula)

    row = 2

    for id in ids_peliculas:
        pelicula = buscar_rating(id)
        # 3 label, title, rating y rating count
        title_label = tk.Label(frame, text=f"Titulo: {pelicula[0]}")
        rating = tk.Label(frame, text=f"Rating: {pelicula[1]}")
        rating_count = tk.Label(frame, text=f"Cantidad de Calificaciones: {pelicula[2]}")
        title_label.grid(row=row, column=0)
        rating.grid(row=row, column=1)
        rating_count.grid(row=row, column=2)
        row += 1

    return 
# Interfaz
#Frame
canvas = tk.Canvas(ventana)
frame = tk.Frame(canvas)
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
# Configurar la barra de desplazamiento
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")

# Configurar la barra de desplazamiento
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
# Configurar el Canvas y el Frame
frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")

# Configurar el Canvas
canvas.grid(row=0, column=0, sticky="nsew")
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)



etiqueta_pelicula = tk.Label(frame, text="Ingresa el nombre de la pelicula")
etiqueta_pelicula.grid(row=0, column=0, columnspan=3)




entrada = tk.Entry(frame)
entrada.grid(row=1, column=0, columnspan=2)

# Crear un botón
boton_escribir = tk.Button(frame, text="Buscar", command=buscar_el_rating )
boton_escribir.grid(row=1, column=2)


#Iniciar loop
ventana.mainloop()