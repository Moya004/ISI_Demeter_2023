from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class SearchScreen(Screen):
    def load(self) -> None:
        lastR = getattr(App.get_running_app().alerts.history, "history", [])[-1]
        lastA = App.get_running_app().statsManager.lastRegister
        self.ids.date_last_register.text = f'{lastA.day}/{lastA.month}/{lastA.year}' if lastA is not None else '-/-/-'
        self.ids.time_last_register.text = f'{lastA.hour}:{lastA.minute}:{lastA.second}' if lastA is not None else '-:-:-'
        self.ids.ph.text = f'Ultimo nivel de PH: {lastR[4]}'
        self.ids.temp.text = f'Ultimo nivel de Temp.: {lastR[5]}'
        self.ids.hum.text = f'Ultimo nivel de Humedad: {lastR[6]}'

    def search(self) -> None:
        result = App.get_running_app().cropsManager.search_crop(self.ids.Croptext.text.lower())
        if result is None:
            self.ids.not_found.color = 1, 0, 0, 1
            self.ids.cul_ph.text = ''
            self.ids.cul_temp.text = ''
            self.ids.cul_hum.text = ''
            return
        self.ids.cul_ph.text = f'PH: {getattr(result, "_Cultivo__ph_min", "xd")} a {getattr(result, "_Cultivo__ph_max", "xd")}'
        self.ids.cul_temp.text = f'TEMP.C:{getattr(result, "_Cultivo__temp_min", "xd")} a {getattr(result, "_Cultivo__temp_max", "xd")}'
        self.ids.cul_hum.text = f'HUMEDAD:{getattr(result, "_Cultivo__hum_min", "xd")} a {getattr(result, "_Cultivo__hum_max", "xd")}'


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class BgCanvas(Widget):
    pass


Builder.load_file('searchscreen.kv')