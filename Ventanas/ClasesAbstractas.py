from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from abc import abstractmethod

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

