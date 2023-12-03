from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class HomeScreen(Screen):
    pass


class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass


class BgCanvas(Widget):
    pass


Builder.load_file('HomeScreen.kv')