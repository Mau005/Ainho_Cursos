from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager


from Ventanas.ClasesAbstractas import ABScreen
from Ventanas.Cursos import Cursos
from Ventanas.Cursos import ContenidoCurso

import Core.Herramientas as tl
import Core.Constantes as cn

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

class Inicio(ABScreen):
    manejador_sub_ventanas = ObjectProperty()

    def __init__(self, nombre, manejador_main,**args):
        super().__init__(nombre, **args)
        self.manejador_main = manejador_main
        self.cursos = Cursos("cursos",self.manejador_sub_ventanas)
        self.agregar_sub_ventanas(self.cursos)
        self.procesar_paginas()

    def procesar_paginas(self):
        for cursos in self.cursos.lista_cursos.keys():
            self.manejador_sub_ventanas.add_widget(ContenidoCurso(cursos,self.cursos.lista_cursos[cursos],self.manejador_sub_ventanas))

    def agregar_sub_ventanas(self, objeto):
        self.manejador_sub_ventanas.add_widget(objeto)

    def siguiente(self, nombre):
        pass

    def actualizar(self, dt):
        pass
