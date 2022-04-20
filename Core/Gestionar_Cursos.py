import os
from kivy.uix.scrollview import ScrollView

from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList
from kivymd.uix.screen import MDScreen
from Core.Constantes import RUTA_ERROR_IMAGEN


class ModMDLabel(MDLabel):
    def __init__(self,**kargs):
        super().__init__(**kargs)
        self.halign = "center"
        self.size_hint_y= None


class Gestionar_Cursos:
    """
    Clase echa para gestionar la ventana de cada pagina del curso
    """
    @classmethod
    def __cargar_curso(cls,ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as contenido:
                return contenido.readlines()
        except FileNotFoundError as error:
            print(f"Error al cargar la ruta mencionada {error}")
            return None

    @classmethod
    def __gestiona_pagina(self,id_pagina,secuencia_curso,botones):

        contenedor = MDScreen(name=str(id_pagina))
        carta = MDCard(size_hint= [.9, .85], pos_hint = {"center_x": 0.5, "center_y": 0.5})
        scrollview = ScrollView(bar_width=10, do_scroll_x=False)
        mdlist = MDList(padding="30dp")
        for objetos in secuencia_curso:
            mdlist.add_widget(objetos)
        scrollview.add_widget(mdlist)
        carta.add_widget(scrollview)


        contenedor.add_widget(carta)
        contenedor.add_widget(botones)
        return contenedor

    @classmethod
    def cargar_cursos(cls,id_pagina,carpeta,archivo,botones):
        secuencia_curso = []
        buscar_secuencia = ""
        control_buscar = False
        control_ciclos = 7
        ruta = f"{carpeta}/{archivo}"
        contenido = cls.__cargar_curso(ruta)

        for lineas in contenido:
            for caracter in lineas:
                buscar_secuencia += caracter
                if buscar_secuencia == "IMAGEN":
                    control_buscar = True
                    contenido = lineas.split("=")[1].replace('"', "").replace(" ","").replace("\n","")
                    ruta = f"{carpeta}/Imagenes/{contenido}"
                    if os.path.exists(ruta):
                        secuencia_curso.append(FitImage(source=ruta, size_hint_y=None, height="450dp"))
                    else:
                        secuencia_curso.append(FitImage(source=RUTA_ERROR_IMAGEN, size_hint_y=None, height="450dp"))
                    break
                elif buscar_secuencia == "TITULO":
                    contenido = lineas.split("=")[1].replace('"', "")
                    control_buscar = True
                    secuencia_curso.append(ModMDLabel(text = contenido,font_style = "H2"))
                    break
                elif buscar_secuencia == "##":
                    control_buscar = True
                    break
                elif len(buscar_secuencia) >= control_ciclos:
                    break
            buscar_secuencia = ""
            if control_buscar:
                control_buscar = False
            else:
                if lineas != "\n":
                    secuencia_curso.append(MDLabel(text = lineas, size_hint_y = None))
        return cls.__gestiona_pagina(id_pagina, secuencia_curso,botones)
