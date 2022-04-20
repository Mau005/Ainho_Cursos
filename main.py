from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from Ventanas.SubVentanas import Ingresos, Inicio, RegistrarUsuarios

Builder.load_file("Ventanas/main.kv")

class AinhoCursos(MDApp):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.ventanas = {}
        self.manejador = ScreenManager() #Encargadod de gestionar toda las ventanas principales
        self.configurar_variables()

    def configurar_variables(self):
        self.ingresos = Ingresos("ingreso")
        self.inicio = Inicio("inicio",self.manejador)
        self.registrar = RegistrarUsuarios("registrar")

        self.registrar_ventana(self.ingresos)
        self.registrar_ventana(self.inicio)
        self.registrar_ventana(self.registrar)

    def registrar_ventana(self,objeto):
        self.ventanas.update({objeto.name:objeto})
        self.manejador.add_widget(objeto)

    def build(self):
        self.title = "Ainho Cursos v1.0 Beta"
        return self.manejador


if __name__ == "__main__":
    AinhoCursos().run()