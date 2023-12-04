from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

class AlertMoreScreen(Screen):
    pass

class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

class BgCanvas(Widget):
    pass

class DropDown_Year3(BoxLayout):
    pass

class DropDown_Mes3(BoxLayout):
    pass

Builder.load_file('alertmore.kv')