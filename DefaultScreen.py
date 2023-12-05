from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class DefaultScreen(Screen):
    pass

class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class BgCanvas(Widget):
    pass


Builder.load_file('DefaultScreen.kv')