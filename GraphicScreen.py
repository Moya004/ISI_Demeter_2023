from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from math import sqrt

class GraphicScreen(Screen):

    def load(self) -> None:
        self.ids.select_mes.ids.selected_month_label.text = 'Seleccione el mes'
        self.ids.select_year.ids.selected_year_label.text = 'Seleccione el año'
        self.ids.ph_prom.text = f'PH PROMEDIO'
        self.ids.temp_prom.text = f'TEMPERATURA PROMEDIO'
        self.ids.hum_prom.text = f'HUMEDAD PROMEDIO'
        self.ids.dv_ph.text = f'DESVIACION EST. PH'
        self.ids.dv_temp.text = f'DESVIACION EST. TEMPERATURA'
        self.ids.dv_hum.text = f'DESVIACION EST. HUMEDAD'


    def promedio(self, data: list) -> tuple:
        n = len(data)
        prom_ph = 0.0
        prom_temp = 0.0
        prom_hum = 0.0
        if n <= 0:
            return 0.0, 0.0, 0.0
        for i in data:
            prom_ph += float(i[4])
            prom_temp += float(i[5])
            prom_hum += float(i[6])

        return prom_ph/n, prom_temp/n, prom_hum/n

    def desviacion(self, data: list, promedios: tuple) -> tuple:
        n = len(data)
        dv_ph = 0.0
        dv_temp = 0.0
        dv_hum = 0.0
        if n <= 0:
            return 0.0, 0.0, 0.0
        for i in data:
            dv_ph += (float(i[4]) - promedios[0]) ** 2
            dv_temp += (float(i[5]) - promedios[1]) ** 2
            dv_hum += (float(i[6]) - promedios[2]) ** 2
        dv_ph /= n - 1
        dv_temp /= n - 1
        dv_hum /= n - 1

        return sqrt(dv_ph), sqrt(dv_temp), sqrt(dv_hum)


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

        promedios = self.promedio(reg)
        desviacion = self.desviacion(reg, promedios)
        dp = round(desviacion[0], 3)
        dt = round(desviacion[1], 3)
        dh = round(desviacion[2], 3)

        self.ids.ph_prom.text = f'PH PROMEDIO: {promedios[0]}'
        self.ids.temp_prom.text = f'TEMPERATURA PROMEDIO: {promedios[1]}'
        self.ids.hum_prom.text = f'HUMEDAD PROMEDIO: {promedios[2]}'
        self.ids.dv_ph.text = f'DESVIACION EST. PH: {dp}'
        self.ids.dv_temp.text = f'DESVIACION EST. TEMPERATURA {dt}'
        self.ids.dv_hum.text = f'DESVIACION EST. HUMEDAD {dh}'



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