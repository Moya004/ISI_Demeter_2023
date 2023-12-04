from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class IdentifyScreen(Screen):

    def verify(self, id: str) -> None:
        ag = App.get_running_app().loginManager.checkIfExist(id)
        if ag is None:
            self.ids.dont_exist.color = 1, 0, 0
        else:
            App.get_running_app().usr = ag
            self.ids.dont_exist.color = 1, 1, 1
            self.parent.parent.push("Reset")


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


Builder.load_file('identifyscreen.kv')
