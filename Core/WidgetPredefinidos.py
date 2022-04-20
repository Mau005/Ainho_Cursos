from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDIcon
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from Core.Constantes import CONTROL_RANGOS

class BotonVolverInicio(MDBoxLayout):
    def __init__(self,paginas,volver, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None 
        self.height = "25dp"
        self.spacing = "20dp"
        self.pos_hint = {"center_x": 1, "center_y": 0.03}
        self.paginas = paginas
        self.volver = volver
        self.btn = MDRectangleFlatButton(text = "Volver", on_release = self.siguiente)
        self.add_widget(self.btn)
        
    def siguiente(self, *Args):
        print(self.volver)
        self.paginas.current = self.volver
    
class BotonCurso(MDBoxLayout):
    def __init__(self, id_curso_principal, nombre, descr, carpeta,rango, paginas, **kwargs):
        super().__init__(**kwargs)
        self.id_curso_principal = id_curso_principal
        self.size_hint_y = None
        self.height= "35dp"
        self.spacing = "20dp"
        self.id_pagina = f"{nombre}.1"
        self.nombre = nombre
        self.descr = descr
        self.carpeta = carpeta
        self.paginas = paginas
        self.rango = rango
        self.icono = MDIcon(icon = "")
        self.boton = MDTextButton(pos_hint={"center_x": 1, "center_y": 0.5}, text=self.nombre, on_release=self.siguiente)
        self.check = MDCheckbox()
        self.add_widget(self.icono)
        self.add_widget(self.boton)
        self.add_widget(self.check)

    def siguiente(self, *args):
        self.paginas.current = self.id_pagina


class BotonSiguiente(MDBoxLayout):
    def __init__(self,manejador, se_encuentra,clase,minimo, maximo,defecto = "1", **kwargs):
        super().__init__(**kwargs)
        self.manejador = manejador
        self.se_encuentra = se_encuentra
        self.minimo = minimo
        self.maximo = maximo 
        self.clase = clase
        self.defecto = defecto

        self.size_hint_y = None 
        self.height = "25dp"
        self.spacing = "20dp"
        self.pos_hint = {"center_x": 1, "center_y": 0.03}
        self.btn1  = MDRectangleFlatButton(text = "Atras", on_release = self.volver)
        self.btn2 = MDRectangleFlatButton(text = "Volver a Menu",on_release = self.default)
        self.btn3 = MDRectangleFlatButton(text = "Siguiente", on_release = self.siguiente)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)

    def default(self,*args):
        self.manejador.current = self.defecto

    def volver(self,*args):
        procesar = self.se_encuentra -1
        if procesar >= self.minimo and procesar <= self.maximo:
            self.manejador.current = f"{self.clase}.{str(procesar)}"

    def siguiente(self, *arg):
        procesar = self.se_encuentra +1
        if procesar >= self.minimo and procesar <= self.maximo:
            self.manejador.current = f"{self.clase}.{str(procesar)}"