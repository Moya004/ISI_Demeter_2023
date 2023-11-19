from kivy.uix.screenmanager import ScreenManager

#aqui basicamente segui lo del video para establecer el movimiento de los screem
#esto basicamente sigue el comportamiento de un stack por eso se inicializo una
class NavigationScreenManager(ScreenManager):
    screens_stack = []
    def push(self , screen_name):
        if screen_name not in self.screens_stack:
            self.screens_stack.append(self.current)
            #aqui defini la direccion en la que cambia el screen a otro
            self.transition.direction = "left"
            self.current = screen_name


    def pop(self):
        if len(self.screens_stack) > 0:
            screen_name = self.screens_stack[-1]
            del self.screens_stack[-1]
            # aqui defini la direccion en la que cambia el screen a otro
            self.transition.direction = "right"
            self.current = screen_name

#para quer entiendas mejor revisa el video de NavigationScreenManager que explica mejor esto
#pero basicamente y hasta donde capto esto te ahorra el estar escribiendo en demeter.kv el nombre
#de la screem a la que cambia y en que direccion asi que en demeter.kv solo nombras las screem y asignas a los botones
#de cada screem a donde se debe mover y como es un stack para retornar a la anterior screen se realiza un pop y para ir
#a otra realizas un push