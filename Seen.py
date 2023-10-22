from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from manageBD import LogIn


class LogInLayout(FloatLayout):

    def login_click(self, cc: str, pas: str) -> None:
        print(LogIn().connect(cc, pas))


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class DemeterApp(App):
    pass
