from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class AlertMoreScreen(Screen):

    def display(self) -> None:
        urg = getattr(App.get_running_app().alerts.history, "history", [])[:]
        crops = App.get_running_app().crops
        crops_names = {}
        for m in crops:
            crops_names[getattr(m, "_Cultivo__id", 'xd')] = getattr(m, "_Cultivo__name", 'Fuk')


        for i in urg:
            self.ids.to_display.text = self.ids.to_display.text + f'Problema con {crops_names[i[1]]}: el {i[2].day}/{i[2].month}/{i[2].year} a las {i[3].hour}:{i[3].minute}:{i[3].second}\n\n'

    def unload(self) -> None:
        self.ids.to_display.text = ''

class BackgroundColor(Widget):
    pass

class BgLabel(Label, BackgroundColor):
    pass

class BgCanvas(Widget):
    pass

class DropDown_Year3(BoxLayout):
    pass

class DropDown_Mes3(BoxLayout):
    pass

Builder.load_file('alertmore.kv')