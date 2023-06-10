import tkinter as tk
import random

lista_palabras = [
    "manzana", "perro", "gato", "casa", "sol", "luna", "pelota", "árbol", "libro", "mesa", 
    "silla", "carro", "planta", "ciudad", "parque", "río", "playa", "montaña", "avión", 
    "tren", "barco", "bolsa", "zapato", "camisa", "pantalón", "sombrero", "guitarra", 
    "piano", "flor", "diente", "hoja", "taza", "plato", "cuchara", "tenedor", "cuchillo", 
    "teléfono", "ordenador", "televisión", "lápiz", "bolígrafo", "pintura", "pincel", 
    "corazón", "nube", "estrella", "fruta", "vegetal", "película", "música", "baile", 
    "fútbol", "baloncesto", "tenis", "gimnasia", "nadar", "correr", "saltar", "dormir", 
    "comer", "beber", "amar", "odiar", "alegría", "tristeza", "enojo", "miedo", "sorpresa",
    "risa", "llanto", "risa", "amigo", "familia", "amor", "vida", "sueño", "viaje", "fiesta",
    "risa", "poema", "historia", "alegría", "reír", "caminar", "abrazo", "beso", "canción",
    "esperanza", "magia", "mariposa", "libertad", "sabiduría", "paz", "justicia", "creatividad",
    "inspiración", "éxito", "felicidad", "alegría", "amabilidad", "generosidad", "sueño",
    "aventura", "maravilla", "travesura", "asombro", "gratitud", "celebración", "esplendor",
    "satisfacción", "júbilo", "emoción", "feliz", "diversión", "apasionado", "hermoso",
    "extraordinario", "radiante", "encantador", "maravilloso", "brillante", "encantado",
    "espléndido", "fantástico", "mágico", "espectacular", "increíble", "notable", "estupendo",
    "admirable", "deslumbrante", "gracioso", "divino", "glorioso", "triunfante", "triunfo",
    "espléndido", "triunfador", "triunfo", "triunfador", "logro", "triunfar", "triunfal",
    "gloria", "victoria", "exitoso", "exitoso", "celebrar", "éxito", "grueso", "vencedor",
    "victoria", "victorioso", "vencedor", "victoria", "victorioso", "tren", "locomotora", 'virote']

palabra_elegida = lista_palabras[random.randrange(0, len(lista_palabras))]
etiquetas_letras = []
letras_falladas = []
vidas = 3

#Funcion de elegir letra
def elegir_letra():
    letra = entrada.get()
    entrada.config(text="")
    if(letra in palabra_elegida):
        for index, l in enumerate(palabra_elegida):
            if(l == letra):
                etiquetas_letras[index].config(text=letra)
    else:
        global vidas
        vidas -= 1
        etiqueta_vidas.config(text=f"Cantidad de vidas {vidas}")

        letras_falladas.append(letra)
        etiqueta_letras_falladas.config(text=f"{etiqueta_letras_falladas['text']}, {letra}")
        if(vidas == 0): 
            derrota()
    
    caracteres = list(map(lambda label: label.cget('text') ,etiquetas_letras))
    if '_' not in caracteres:
        victoria()
    return 

def preparar_entorno():
    boton_iniciar.destroy()
    col = 0
    for letra in palabra_elegida:
        etiqueta_letra = tk.Label(frame, text="_")
        etiqueta_letra.grid(row=2, column=col)
        etiquetas_letras.append(etiqueta_letra)
        col += 1
    print(palabra_elegida)
    return

def derrota():
    etiqueta_entry_letra.destroy()
    etiqueta_vidas.destroy()
    boton_buscar.destroy()
    etiqueta_letras_falladas.destroy()
    list(map(lambda etiqueta: etiqueta.destroy(), etiquetas_letras))
    etiqueta_perdiste = tk.Label(ventana, text="PERDISTE")
    etiqueta_perdiste.grid(row=3, column=0)
    print('perdiste')
    

def victoria():
    etiqueta_entry_letra.destroy()
    entrada.destroy()
    etiqueta_vidas.destroy()
    boton_buscar.destroy()
    etiqueta_letras_falladas.destroy()
    etiqueta_ganaste = tk.Label(ventana, text="GANASTE")
    etiqueta_ganaste.grid(row=0, column=0)
    print('ganaste')


#Interfaz
#Ventana
ventana = tk.Tk()
ventana.title('Juego del Ahorcado')
ventana.geometry("600x400")

frame = tk.Frame()
frame.grid(row=2, column=1)

#label
etiqueta_entry_letra = tk.Label(ventana, text="Ingresa la letra a buscar")
etiqueta_entry_letra.grid(row=0, column=0)


#LEtras falladas
etiqueta_letras_falladas = tk.Label(ventana, text='Letras fallasdas: ')
etiqueta_letras_falladas.grid(row=3,column=0)
#input
entrada = tk.Entry(ventana)
entrada.grid(row=1,column=0)

#vidas
etiqueta_vidas= tk.Label(ventana, text=f"Cantidad de vidas {vidas}")
etiqueta_vidas.grid(row=0, column=1)
# Crear un botón
boton_buscar = tk.Button(ventana, text="Buscar", command=elegir_letra )
boton_buscar.grid(row=1, column=1)

# Crear un botón
boton_iniciar = tk.Button(ventana, text="Iniciar", command=preparar_entorno , width=30)
boton_iniciar.grid(row=2, column=0, columnspan=2)
#Iniciar loop
ventana.mainloop()




