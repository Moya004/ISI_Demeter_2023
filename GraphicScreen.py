from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class GraphicScreen(Screen):
    pass

class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

class BgCanvas(Widget):
    pass

class CustomDropdown(FloatLayout):
    pass

class DropDown_Year2(BoxLayout):
    pass

class DropDown_Mes2(BoxLayout):
    pass

Builder.load_file('graphicscreen.kv')