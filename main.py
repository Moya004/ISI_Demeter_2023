from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class LogInFloatLayout(FloatLayout):

    def login_click(self) -> None:
        print('Clicked')


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class DemeterApp(App):
    pass


DemeterApp().run()
