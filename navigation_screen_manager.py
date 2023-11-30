from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class NavigationScreenManager(ScreenManager):

    screens_stack = []

    #Trabaja como stack asi que estos dos metodos me permiten apilar y desapilar
    #apilar
    def push(self , screen_name):
        if screen_name not in self.screens_stack:
            self.screens_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name
            print(f'Agregada pantalla {screen_name} a la pila. Nueva pila: {self.screens_stack}')


    #desapilar
    def pop(self):
        if len(self.screens_stack) > 0:
            screen_name = self.screens_stack[-1]
            del self.screens_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name
            # mensaje a eliminar posteriormente
            print(f'Retirada pantalla {screen_name} de la pila. Nueva pila: {self.screens_stack}')


    #Esto permite que al oprimir un label limpie la pila a excepcion de la ventana a la que regresa
    def pop_to_label(self, target_screen, source_screen):
        while len(self.screens_stack) > 0 and self.current != target_screen:
            self.pop()
        # Aquí puedes realizar acciones específicas según la pantalla de origen
        #mensaje a eliminar posteriormente
        print(f'Redirigiendo desde {source_screen} a {target_screen}')


    #mantener original por si necesitas realizar cambios
    def pop_to(self, target_screen):
        while len(self.screens_stack) > 0 and self.current != target_screen:
            self.pop()


    #permite al identificar que toque el label cambiar de screen
    def handle_touch(self, label_name, target_screen, *args):
        # mensaje a eliminar posteriormente
        print(f'Toqué el Label {label_name}, redirigiendo a {target_screen}')
        print(f'Pila de pantallas después del toque: {self.screens_stack}')

        self.push(target_screen)

