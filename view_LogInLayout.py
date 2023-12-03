from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from manageBD import LogIn, Statistic, CropState
from models import *

class LogInLayout(FloatLayout):
    def login_click(self, cc: str, pas: str) -> None:
        log = LogIn().log(cc, pas)
        data = Statistic()
        cul = CropState()
        if log is not None:
            App.get_running_app().usr = log
            cul.load_crops()
            data.stats(usr=log)
            data.__init__()
            data.search_alerts(usr=log)
            self.ids.LabelCredenciales.color = 1, 1, 1

            self.parent.parent.push("SecondScreen")
        else:
            self.ids.LabelCredenciales.color = 1, 0, 0


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


Builder.load_file('LogInLayout.kv')


class DemeterApp(App):
    usr: Agricultor = Agricultor()
    regis: Estado = Estado()
    alerts: Alerta = Alerta()

    pass
