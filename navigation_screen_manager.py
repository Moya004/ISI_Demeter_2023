from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager):
    screens_stack = []
    def push(self , screen_name):
        if screen_name not in self.screens_stack:
            self.screens_stack.append(self.current)
            self.transition.direction = "left"
            self.current = screen_name


    def pop(self):
        if len(self.screens_stack) > 0:
            screen_name = self.screens_stack[-1]
            del self.screens_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name
