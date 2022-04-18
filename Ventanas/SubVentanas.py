from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen
from abc import abstractmethod

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.swiper import MDSwiperItem


class ABScreen(Screen):
    def __init__(self, nombre, **args):
        super().__init__(**args)
        self.name = nombre

    @abstractmethod
    def actualizar(self, dt):
        pass

    @abstractmethod
    def siguiente(self, nombre):
        self.manager.current = nombre


class Ingresos(ABScreen):
    def __init__(self, nombre, **args):
        super().__init__(nombre, **args)
        self.dialog = None

    def actualizar(self, dt):
        pass

    def limpiar(self):
        self.root.ids.welcome_label.text = "Bienvenido"
        self.root.ids.usuario.text = ""
        self.root.ids.password.text = ""

    def mostrar_registro(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Registrarse",
                buttons=[MDFlatButton(text="CANCEL"),
                         MDFlatButton(text="DISCARD"),
                         ],
            )
        self.dialog.open()

    def siguiente(self, nombre):
        super().siguiente(nombre)


class Inicio(ABScreen):
    def siguiente(self, nombre):
        pass

    def actualizar(self, dt):
        pass

    manejador_sub_ventanas = ObjectProperty()

    def __init__(self, nombre, **args):
        super().__init__(nombre, **args)
        self.cursos = Cursos("cursos")
        self.sub_ventanas = {}

        self.agregar_sub_ventanas(Cursos("cursos"))

    def agregar_sub_ventanas(self, objeto):
        self.sub_ventanas.update({objeto.name: objeto})
        self.manejador_sub_ventanas.add_widget(objeto)


class Cursos(ABScreen):
    def siguiente(self, nombre):
        pass

    def actualizar(self, dt):
        pass

    contenedor_imagenes = ObjectProperty()

    def __init__(self, nombre, **args):
        super().__init__(nombre, **args)
        #https://c.pxhere.com/photos/a5/f4/startup_start_up_notebooks_creative_computer_company_laptops_display-764684.jpg!d
        #self.contenedor_imagenes.add_widget(SwiperObjectos(source="Assets/Cursos/Hardware/Imagenes/logo.png",
        #                                                   nombre="Curso de Hardware Resumenes Cisco"))
        self.contenedor_imagenes.add_widget(SwiperObjectos(source="https://c.pxhere.com/photos/a5/f4/startup_start_up_notebooks_creative_computer_company_laptops_display-764684.jpg!d",
                                                           nombre="Curso de Hardware Resumenes Cisco"))


class RegistrarUsuarios(ABScreen):
    def actualizar(self, dt):
        pass

    def __init__(self, nombre, **args):
        super(RegistrarUsuarios, self).__init__(nombre, **args)
        self.maximo_long_caracter = 8
        self.seguridad = "!#$%&/()=?._-[]*Ñ"

    def siguiente(self, nombre):
        super().siguiente(nombre)

    def procesar_password(self, password):
        for caracter in password:
            if caracter in self.seguridad:
                return True
        return False

    def registrar(self, correo, password, repetir_password):
        if password == repetir_password:
            if len(password) >= self.maximo_long_caracter:
                if self.procesar_password(password):
                    if "@" in correo:
                        print("""
                        Correo: {}
                        Password: {}
                        """.format(correo, password))
                    else:
                        print("tiene que ser un correo correcto.")
                else:
                    print(f"La contraseña tiene que tener almenos un caracter especial: {self.seguridad}")
            else:
                print("la Longitud de la contraseña tiene que ser mayor a 8")
        else:
            print("El password tiene que ser igual")


class SwiperObjectos(MDSwiperItem):
    source = StringProperty()

    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.ids.nombre.text = nombre


class ListaCursos(ABScreen):
    contenedor = ObjectProperty()

    def __init__(self, nombre, nombre_curso, **args):
        super(ListaCursos, self).__init__(**args)
        self.name = nombre
        self.ids.toolbar.title = nombre_curso

    def actualizar(self, dt):
        pass

    def siguiente(self, nombre):
        super(ListaCursos, self).siguiente(nombre)
