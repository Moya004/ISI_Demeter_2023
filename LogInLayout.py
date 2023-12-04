from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from manageBD import LogIn, Statistic, CropState
from models import *


class LogInLayout(FloatLayout):
    def login_click(self, cc: str, pas: str) -> None:
        log = App.get_running_app().loginManager.log(cc, pas)
        data = App.get_running_app().statsManager.stats(log) if log else None
        alert = App.get_running_app().statsManager.search_alerts(log) if log else None
        cul = App.get_running_app().cropsManager.load_usr_crops(log) if log else None
        if log is not None:
            App.get_running_app().usr = log
            App.get_running_app().crops = cul
            App.get_running_app().regis = data
            App.get_running_app().alerts = alert
            self.ids.LabelCredenciales.color = 1, 1, 1

            self.parent.parent.push("SecondScreen")
        else:
            self.ids.LabelCredenciales.color = 1, 0, 0


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


Builder.load_file('loginlayout.kv')


class DemeterApp(App):
    usr: Agricultor = Agricultor()
    regis: Estado = Estado()
    alerts: Alerta = Alerta()
    crops: set[Cultivo] = set()
    loginManager: LogIn = LogIn()
    cropsManager: CropState = CropState()
    statsManager: Statistic = Statistic()

    def __str__(self) -> str:
        return f'User:{self.usr.__str__()}\nDatos:{self.regis.__str__()}\nAlertas:{self.alerts.__str__()}\nCultivos:{self.crops.__str__()}'
    pass
