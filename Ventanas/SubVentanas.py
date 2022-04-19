from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.swiper import MDSwiperItem

import Core.Herramientas as tl
from abc import abstractmethod
import Core.Constantes as cn


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
                buttons=[MDFlatButton(text="Cancela"),
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
        self.cursos = tl.cargar_cursos()
        self.configurar_cursos()


    def configurar_cursos(self):
        if self.cursos != None:
            for id_curso in self.cursos.keys():
                obj = SwiperObjectos(id_curso,
                self.cursos[id_curso]["titulo"], 
                self.cursos[id_curso]["descr"], 
                self.cursos[id_curso]["carpeta"], 
                self.cursos[id_curso]["logo"])
                self.contenedor_imagenes.add_widget(obj)
        else:
            print("No se pudo cargar los cursos por problemas de recopilacion de datos")

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

    def __init__(self, id_curso, titulo, descr, carpeta, logo, **kwargs):
        super().__init__(**kwargs)
        
        self.id_curso = id_curso
        self.titulo = titulo
        self.descr = descr
        self.ids.nombre.text = self.titulo + self.descr
        
        self.carpeta = carpeta
        self.logo = logo
        
        ruta = f"{cn.RUTA_DEFECTO}/{self.carpeta}/{self.logo}" 


        if tl.archivo_existe(ruta):
            self.source = ruta
        else:
            self.source = f"{cn.RUTA_DEFECTO}/error.png"


class ContenidoCurso(ABScreen):
    contenedor = ObjectProperty()

    def __init__(self, nombre, nombre_curso, **args):
        super(ContenidoCurso, self).__init__(**args)
        self.name = nombre
        self.ids.toolbar.title = nombre_curso

    def actualizar(self, dt):
        pass

    def siguiente(self, nombre):
        super(ContenidoCurso, self).siguiente(nombre)
