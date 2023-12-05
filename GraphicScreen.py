from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class GraphicScreen(Screen):

    def promedio(self, data: list) -> tuple:
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

    def fetch(self) -> None:
        mes = self.ids.select_mes.ids.selected_month_label.text
        anio = self.ids.select_year.ids.selected_year_label.text

        if mes == 'Seleccione el mes' or anio == 'Seleccione el año':
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
        reg = App.get_running_app().statsManager.get_registers_given_date(App.get_running_app().usr, anio,
                                                                                 mapp[mes])
        alt = App.get_running_app().statsManager.get_alerts_given_date(App.get_running_app().usr, anio,
                                                                                 mapp[mes])
        promedios = self.promedio(reg)
        n_reg = len(reg)
        n_alt = len(alt)
        if n_reg == 0:
            ratio = 0
        else:
            ratio = n_alt / n_reg
        self.ids.ph_prom.text = f'PH PROMEDIO: {promedios[0]}'
        self.ids.temp_prom.text = f'TEMPERATURA PROMEDIO{promedios[1]}'
        self.ids.hum_prom.text = f'HUMEDAD PROMEDIO{promedios[2]}'
        self.ids.num_regis.text = f'NUMERO DE REGISTROS: {n_reg*100}%'
        self.ids.num_alert.text = f'NUMERO DE ALERTAS: {n_alt*100}%'
        self.ids.prc_alert.text = f'PORCENTAJE DE ALETTAS: {ratio*100}%'


class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

class BgCanvas(Widget):
    pass

class CustomDropdown(FloatLayout):
    pass

class DropDown_Year2(BoxLayout):
    pass

class DropDown_Mes2(BoxLayout):
    pass

Builder.load_file('graphicscreen.kv')