from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from manageBD import LogIn


class LogInLayout(FloatLayout):
    def login_click(self, cc: str, pas: str) -> None:
        print(LogIn().Log(cc, pas))


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


Builder.load_file('LogInLayout.kv')


class DemeterApp(App):
    pass
