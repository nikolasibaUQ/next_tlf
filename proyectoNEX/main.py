import CrearAutomata
from tokens.EnumPalabras import Token

def procesar_lineas_archivo(nombre_archivo):
    tokens = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for indice, linea in enumerate(archivo, start=1):
                palabra = linea.strip()
                palabra = palabra.split()[0]
                try:
                    token = Token(palabra)
                    tokens.append('Indice: ' + str(indice) + ' ' + 'Subcategoria: ' + str(token.categoria) + ' ' + 'Token: ' + str(palabra))
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