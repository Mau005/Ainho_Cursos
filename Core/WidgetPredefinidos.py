from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDIcon
from kivymd.uix.selectioncontrol import MDCheckbox


class WidgetPredeFinidos:

    @classmethod
    def Contenido_Lista_Cursos(cls,titulo, func_concurrido = None):
        contenedor = MDBoxLayout(size_hint_y = None, height= "35dp", spacing = "20dp")
        icono = MDIcon(icon = "")
        if func_concurrido != None:
            boton = MDTextButton(pos_hint={"center_x": 1, "center_y": 0.5}, text=titulo, on_release=func_concurrido)
        else:
            boton = MDTextButton(pos_hint = {"center_x": 1, "center_y": 0.5}, text= titulo)
        check = MDCheckbox()
        contenedor.add_widget(icono)
        contenedor.add_widget(boton)
        contenedor.add_widget(check)
        return contenedor