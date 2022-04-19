from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from Core.Gestionar_Cursos import Gestionar_Cursos

Builder.load_file("Ventanas/test.kv")


class Ventana(MDScreen):
    contenedor = ObjectProperty()
    pass
class Test(MDApp):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.manejador = ScreenManager()
        self.manejador.add_widget(Ventana())
        self.ventana = Ventana()
        self.manejador.add_widget(self.ventana)
        self.gestionar_cursos = Gestionar_Cursos()
        gestionar = self.gestionar_cursos.get_secuencia()
        for objetos in gestionar:
            self.ventana.contenedor.add_widget(objetos)

    def build(self):
        return self.manejador

if __name__ == "__main__":
    Test().run()