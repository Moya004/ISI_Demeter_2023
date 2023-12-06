from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class HomeScreen(Screen):

    def promedio(self) -> tuple:
        data = getattr(App.get_running_app().regis.history, "history", "xd")
        n = len(data)
        prom_ph = 0.0
        prom_temp = 0.0
        prom_hum = 0.0
        for i in data:
            prom_ph += float(i[4])
            prom_temp += float(i[5])
            prom_hum += float(i[6])
        if n <= 0:
            return 0.0, 0.0, 0.0
        return prom_ph/n, prom_temp/n, prom_hum/n

    def ale(self) -> tuple:
        if len(App.get_running_app().regis) == 0:
            return 0.0, 0.0, 0.0
        return len(App.get_running_app().regis), len(App.get_running_app().alerts), len(App.get_running_app().alerts)/len(App.get_running_app().regis)
    def load(self) -> None:
        to_display_est = self.promedio()
        to_display_al = self.ale()
        self.ids.est_1.text = f'PH GENERAL MEDIO: {round(to_display_est[0], 3)}'
        self.ids.est_2.text = f'TEMP. GENERAL MEDIO: {round(to_display_est[1], 3)}'
        self.ids.est_3.text = f'HUMEDAD GENERAL MEDIO: {round(to_display_est[2], 3)}'
        self.ids.al_1.text = f'CANTIDAD DE REGISTROS: {round(to_display_al[0], 3)}'
        self.ids.al_2.text = f'CANTIDAD DE ALERTAS: {round(to_display_al[1], 3)}'
        self.ids.al_3.text = f'PORCENTAJE DE ALERTAS: {round(to_display_al[2], 3) * 100}%'


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class BgCanvas(Widget):
    pass


Builder.load_file('homescreen.kv')