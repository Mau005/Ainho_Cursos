



class Config_Cursos():
    def __init__(self):
        self.lista_cursos = {}


        estructura = {
            1: {
                "titulo": "Hardware Cisco 1-3",
                "descr": "breve introduccion",
                "Contenido": {
                    1: {"titulo": "Capitulo 1 Tu Hermana",
                        "ruta": "Hardware/1.cia"},
                    2:{"titulo": "capitulo 2 la venganza de tu hermana",
                       "ruta": "Hardware/2.cia"}
                }
            },
            2:{
                "titulo": "Fundamentos de base De Datos",
                "descr": "breve introduccion",
                "contenido":{
                    1: {"titulo": "Capitulo 1 La venganza del perla negra",
                        "ruta": "FundamentosBD/1.cia"},
                    2: {"titulo": "capitulo 2 el retorno del rey",
                        "ruta": "FundamentosBD/2.cia"}
                }
            }
        }
    def agregar_curso(self,key,objeto):
        self.lista_cursos.update({key:objeto})