import json, os
from Core.Constantes import RUTA_LISTA_CURSOS

def cargar_cursos():
    """
    Se encarga de Cargar el JSON para encontrar los archivos de los cursos
    :return:
    """
    try:
        with open(RUTA_LISTA_CURSOS, "r") as contenido:
            print("Entro=")
            return json.load(contenido)
    except FileNotFoundError as error:
        print(f"El archivo no se ha encontrado error: {error}")
        return None

def archivo_existe(ruta):
    return os.path.exists(ruta)