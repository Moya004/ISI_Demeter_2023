from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class AlertScreen(FloatLayout):
    pass

class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

class BgCanvas(Widget):
    pass

class DropDown_Year(BoxLayout):
    pass

class DropDown_Mes(BoxLayout):
    pass

Builder.load_file('alertsscreen.kv')