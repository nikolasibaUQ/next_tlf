import os

import CrearAutomata
from tokens.EnumPalabras import Token
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class main:
    def __init__(self, root):

        self.root = root
        self.root.title("Autómatas Generados")

        pantalla_ancho = root.winfo_screenwidth()
        pantalla_alto = root.winfo_screenheight()

        ventana_ancho = int(pantalla_ancho * 0.8)
        ventana_alto = int(pantalla_alto * 0.8)

        pos_x = (pantalla_ancho // 2) - (ventana_ancho // 2)
        pos_y = (pantalla_alto // 2) - (ventana_alto // 2)

        root.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        directorio_base = os.path.join(directorio_actual, "automathon")
        subdirectorios = [nombre for nombre in os.listdir(directorio_base) if
                          os.path.isdir(os.path.join(directorio_base, nombre))]

        frame = ttk.Frame(notebook)
        notebook.add(frame, text="informacion")

        tokens = procesar_lineas_archivo('operaciones.txt')

        columns = ('indice', 'subcategoria', 'token')
        self.tree = ttk.Treeview(frame, columns=columns, show='headings')

        self.tree.heading('indice', text='Índice')
        self.tree.heading('subcategoria', text='Subcategoría')
        self.tree.heading('token', text='Token')

        self.tree.column('indice', width=100)
        self.tree.column('subcategoria', width=200)
        self.tree.column('token', width=200)

        self.tree.pack(fill='both', expand=True)

        # Insertar datos
        for token in tokens:
            partes = token.split(' ')
            indice = partes[1]
            subcategoria = partes[3]
            token_val = ' '.join(partes[5:])
            self.tree.insert('', tk.END, values=(indice, subcategoria, token_val))

        #pestañas de los automatas
        for subdir in subdirectorios:
            ruta_completa = os.path.join(directorio_base, subdir)
            self.crear_pestana(notebook, subdir, ruta_completa)

    def crear_pestana(self, notebook, titulo, ruta):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=titulo)

        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scroll_y.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        image_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=image_frame, anchor="nw")

        for archivo in os.listdir(ruta):
            if archivo.endswith(".png"):
                img_path = os.path.join(ruta, archivo)
                image = Image.open(img_path)
                photo = ImageTk.PhotoImage(image)

                label = tk.Label(image_frame, image=photo)
                label.image = photo
                label.pack()


def procesar_lineas_archivo(nombre_archivo):
    tokens = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for indice, linea in enumerate(archivo, start=1):
                palabra = linea.strip()
                palabra = palabra.split()[0]
                try:
                    token = Token(palabra)
                    tokens.append('Indice: ' + str(indice) + ' ' + 'Subcategoria: ' + str(
                        token.categoria) + ' ' + 'Token: ' + str(palabra))
                    CrearAutomata.CrearAutomata.mostrar_automata(palabra, token.categoria, indice)
                except ValueError as e:
                    print(f"Error en la línea {indice}: {e}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except IOError:
        print(f"Hubo un error al leer el archivo {nombre_archivo}.")
    return tokens


# Llamar a la función con el nombre del archivo
tokens = procesar_lineas_archivo('operaciones.txt')
for token in tokens:
    print(token)

if __name__ == "__main__":
    root = tk.Tk()
    app = main(root)
    root.mainloop()
