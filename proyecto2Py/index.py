"""
Este script va a devolver las paletas de colores populares
de la pagina colorhunt y sus respectivos likes ademas la 
app de tkinker va a ser coloreada con la paleta mas popular
"""
import tkinter as tk
import requests
from bs4 import BeautifulSoup


#Logica
def buscar_ofertas():
    url = 'https://www.mercadolibre.com.ar/ofertas#nav-header'
    # Realizar la solicitud HTTP GET a la URL
    response = requests.get(url)
    # Crear el objeto BeautifulSoup con el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar todos los elementos de los artículos
    items = soup.find_all('div', class_='promotion-item__description')

    # Iterar sobre cada artículo y extraer el nombre y el precio
    boton_buscar.destroy()
    row = 1
    for item in items:
        # Extraer el nombre del artículo
        name_element = item.find('p', class_='promotion-item__title')
        name = name_element.text.strip() if name_element else "No se encontró nombre"
        name_label = tk.Label(frame, text=name, anchor='w')
        # Extraer el precio del artículo
        price_element = item.find('span', class_='andes-money-amount__fraction')
        price = price_element.text.strip() if price_element else "No se encontró precio"
        price_label = tk.Label(frame, text=price , anchor='w' )

        nombre_label = tk.Label(frame, text="nombre")
        precio_label = tk.Label(frame, text="precio")
        
   
        nombre_label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
        name_label.grid(row=row, column=1, padx=5, pady=5)
        precio_label.grid(row=row, column=2, sticky="e", padx=5, pady=5)
        price_label.grid(row=row, column=3, padx=5, pady=5)

        row += 1



    return
#Interfaz
#Ventana
ventana = tk.Tk()
ventana.title('Web Scrapper ML')
ventana.geometry("1200x400")

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

# Crear un botón
boton_buscar = tk.Button(ventana, text="Buscar ofertas ML", command=buscar_ofertas )
boton_buscar.grid(row=0, column=0)

#Iniciar loop
ventana.mainloop()

"""
Este script va a devolver las paletas de colores populares
de la pagina colorhunt y sus respectivos likes ademas la 
app de tkinker va a ser coloreada con la paleta mas popular
"""
import tkinter as tk
import requests
from bs4 import BeautifulSoup


#Logica
def buscar_ofertas():
    url = 'https://www.mercadolibre.com.ar/ofertas#nav-header'
    # Realizar la solicitud HTTP GET a la URL
    response = requests.get(url)
    # Crear el objeto BeautifulSoup con el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar todos los elementos de los artículos
    items = soup.find_all('div', class_='promotion-item__description')

    # Iterar sobre cada artículo y extraer el nombre y el precio
    boton_buscar.destroy()
    row = 1
    for item in items:
        # Extraer el nombre del artículo
        name_element = item.find('p', class_='promotion-item__title')
        name = name_element.text.strip() if name_element else "No se encontró nombre"
        name_label = tk.Label(frame, text=name, anchor='w')
        # Extraer el precio del artículo
        price_element = item.find('span', class_='andes-money-amount__fraction')
        price = price_element.text.strip() if price_element else "No se encontró precio"
        price_label = tk.Label(frame, text=price , anchor='w' )

        nombre_label = tk.Label(frame, text="nombre")
        precio_label = tk.Label(frame, text="precio")
        
   
        nombre_label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
        name_label.grid(row=row, column=1, padx=5, pady=5)
        precio_label.grid(row=row, column=2, sticky="e", padx=5, pady=5)
        price_label.grid(row=row, column=3, padx=5, pady=5)

        row += 1



    return
#Interfaz
#Ventana
ventana = tk.Tk()
ventana.title('Web Scrapper ML')
ventana.geometry("1200x400")

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

# Crear un botón
boton_buscar = tk.Button(ventana, text="Buscar ofertas ML", command=buscar_ofertas )
boton_buscar.grid(row=0, column=0)

#Iniciar loop
ventana.mainloop()

