from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class AnalysisScreen(Screen):
    def load(self) -> None:
        lastA = App.get_running_app().statsManager.lastRegister
        self.ids.date_last_register.text = f'{lastA.day}/{lastA.month}/{lastA.year}' if lastA is not None else '-/-/-'
        self.ids.time_last_register.text = f'{lastA.hour}:{lastA.minute}:{lastA.second}' if lastA is not None else '-:-:-'

    def fetch(self) -> None:
        log = App.get_running_app().usr
        data = App.get_running_app().statsManager.stats(log) if log else None
        alert = App.get_running_app().statsManager.search_alerts(log) if log else None
        cul = App.get_running_app().cropsManager.load_usr_crops(log) if log else None
        App.get_running_app().crops += cul
        App.get_running_app().regis.update(getattr(data.history, "history", [])[:])
        App.get_running_app().alerts.update(getattr(alert.history, "history", [])[:])
        self.load()
        lastR = getattr(App.get_running_app().alerts.history, "history", [])[-1]
        crops = App.get_running_app().crops
        crops_names = {}
        for m in crops:
            crops_names[getattr(m, "_Cultivo__id", 'xd')] = getattr(m, "_Cultivo__name", 'Fuk')

        self.ids.output.text = (f'DATOS ACTUALIZADOS\n\nNombre Cietifico del cultivo: {lastR[1]}\nNombre comun del '
                                f'cultivo {crops_names[lastR[1]]}\nDATOS RECOLECTADOS\n\nPH : {lastR[4]}\nTEMPERATURA '
                                f'EN CELSIUS : {lastR[5]}\nHUMEDAD RELATIVA : {lastR[6]}')

class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

class BgCanvas(Widget):
    pass

Builder.load_file('analysisscreen.kv')