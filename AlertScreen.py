import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class AlertScreen(Screen):

    def load(self) -> None:
        lastA = App.get_running_app().statsManager.lastAlert
        data = len(App.get_running_app().alerts)
        self.ids.alert_amount.text = f'{data}' if data is not None else '0'
        self.ids.date_last_alert.text = f'{lastA.day}/{lastA.month}/{lastA.year}' if lastA is not None else '-/-/-'
        self.ids.time_last_alert.text = f'{lastA.hour}:{lastA.minute}:{lastA.second}' if lastA is not None else '-:-:-'

    def search_last(self) -> None:
        mes = self.ids.select_mes.ids.selected_month_label.text
        anio = self.ids.select_year.ids.selected_year_label.text

        if mes == 'Seleccione el mes' or anio == 'Seleccione el año':
            self.ids.date_last_register.text = '-/-/-'
            self.ids.time_last_register.text = '-:-:-'
            return
        mapp = {
            'Enero': 1,
            'Frebrero': 2,
            'Marzo': 3,
            'Abril': 4,
            'Mayo': 5,
            'Junio': 6,
            'Julio': 7,
            'Agosto': 8,
            'Septiembre': 9,
            'Octubre': 10,
            'Noviembre': 11,
            'Diciembre': 12
        }
        result = App.get_running_app().statsManager.get_last_register_given_date(App.get_running_app().usr, anio, mapp[mes])
        self.ids.date_last_register.text = f'{result[2].day}/{result[2].month}/{result[2].year}'
        self.ids.time_last_register.text = f'{result[3].hour}:{result[3].minute}:{result[3].second}'
class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class BgCanvas(Widget):
    pass


class DropDown_Year(BoxLayout):
    pass


class DropDown_Mes(BoxLayout):
    pass


Builder.load_file('alertsscreen.kv')