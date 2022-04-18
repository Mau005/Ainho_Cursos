import json

class Cursos():

    def __init__(self):
        self.cursos = self.cargar_cursos()


    def cargar_cursos(self):
        """
        Se encarga de Cargar el JSON para encontrar los archivos de los cursos
        :return:
        """
        try:
            with open("Assets/Cursos/cursos.json", "r") as contenido:
                return json.load(contenido)
        except FileNotFoundError as error:
            print(f"El archivo no se ha encontrado error: {error}")
            return None

    def pedir_curso(self,id_curso):
        if self.cursos != None:
            return self.cursos[str(id_curso)]
        else:
            print(f"No tiene formato el contenido de curso")
            return False

    def cantidad_cursos(self):
        if isinstance(self.cursos,dict):
            return len(self.cursos)
        else:
            return 0