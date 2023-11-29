from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
class CorrectResetScreen(FloatLayout):
    pass
class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

Builder.load_file('Correct_ResetScreen.kv')