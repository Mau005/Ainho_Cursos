from kivy.properties import ObjectProperty
from kivymd.uix.swiper import MDSwiperItem

from Ventanas.ClasesAbstractas import ABScreen

from Core.WidgetPredefinidos import BotonCurso, BotonSiguiente, BotonVolverInicio
from Core.Gestionar_Cursos import Gestionar_Cursos
from Core.Constantes import CONTROL_RANGOS
import Core.Herramientas as tl
import Core.Constantes as cn



class Cursos(ABScreen):
    contenedor_imagenes = ObjectProperty()

    def __init__(self, nombre, manejador_sub_ventanas, **args):
        super().__init__(nombre, **args)
        self.cursos = tl.cargar_cursos()
        self.manejador_sub_ventanas = manejador_sub_ventanas
        self.lista_cursos = {}
        self.configurar_cursos()

    def configurar_cursos(self):
        if self.cursos != None:
            for id_curso in self.cursos.keys():
                self.lista_cursos.update({id_curso:self.cursos[id_curso]["carpeta"]})
                obj = SwiperObjectos(id_curso,
                self.cursos[id_curso]["titulo"], 
                self.cursos[id_curso]["descr"], 
                self.cursos[id_curso]["carpeta"], 
                self.cursos[id_curso]["logo"],
                self.manejador_sub_ventanas)
                self.contenedor_imagenes.add_widget(obj)
        else:
            print("No se pudo cargar los cursos por problemas de recopilacion de datos")

class ContenidoCurso(ABScreen):
    manejador = ObjectProperty()

    def __init__(self, id_nombre, carpeta_curso, manejador_main, **args):
        super().__init__(id_nombre, **args)
        self.carpeta_curso = carpeta_curso
        self.listado = ListaCursos(id_nombre, carpeta_curso, self.manejador,manejador_main)
        self.manejador.add_widget(self.listado)
        
        contenido = self.listado.lista_cursos
        for id_paginas in contenido.keys():
            rangos = contenido[id_paginas].rango
            nombre = contenido[id_paginas].nombre
            carpeta = contenido[id_paginas].carpeta
            
            for pagina in range(rangos[0],rangos[1]+CONTROL_RANGOS):
                btn = BotonSiguiente(self.manejador,pagina,carpeta,rangos[0],rangos[1],defecto = contenido[id_paginas].id_curso_principal)
                ruta = f"{cn.RUTA_DEFECTO}/{self.carpeta_curso}/{carpeta}"
                self.manejador.add_widget(Gestionar_Cursos.cargar_cursos(f"{nombre}.{pagina}",ruta,f"{pagina}.cie",btn))



class Paginas(ABScreen):
    contenedor = ObjectProperty()
    

    def __init__(self, id_capitulo, **args):
        super().__init__(id_capitulo, **args)



class ListaCursos(ABScreen):
    contenedor = ObjectProperty()

    def __init__(self, id_nombre, carpeta_curso, manejador,manejador_main,**args):
        super().__init__(id_nombre, **args)
        ruta = f"{cn.RUTA_DEFECTO}/{carpeta_curso}/curso.json"
        contenido = tl.cargar_cursos(ruta)
        self.manejador = manejador
        self.lista_cursos = {}
        self.manejador_main = manejador_main

        for id_curso in contenido.keys():
            obj = BotonCurso(self.name,
            contenido[id_curso]["nombre"],
            contenido[id_curso]["descr"],
            contenido[id_curso]["carpeta"],
            contenido[id_curso]["rango"],
            self.manejador)

            self.lista_cursos.update({obj.nombre:obj})
            self.contenedor.add_widget(obj)
        self.ids.screen.add_widget(BotonVolverInicio(self.manejador_main,"cursos"))

    def siguiente(self, nombre, *args):
        self.paginas.current = nombre


class SwiperObjectos(MDSwiperItem):
    image = ObjectProperty()
    boton_curso = ObjectProperty()

    def __init__(self, id_curso, titulo, descr, carpeta, logo, paginas, **kwargs):
        super().__init__(**kwargs)
        self.id_curso = id_curso
        self.paginas = paginas
        self.titulo = titulo
        self.descr = descr
        self.ids.informacion.text = self.titulo + self.descr
        self.boton_curso.on_release = self.func_ingresos
        self.carpeta = carpeta
        self.logo = logo
        ruta = f"{cn.RUTA_DEFECTO}/{self.carpeta}/{self.logo}"
        
        if tl.archivo_existe(ruta):
            self.image.source = ruta
        else:
            self.image.source = f"{cn.RUTA_DEFECTO}/error.png"
    
    def func_ingresos(self, *args):
        self.paginas.current  = self.id_curso

