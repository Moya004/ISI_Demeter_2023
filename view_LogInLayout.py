from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from manageBD import LogIn


class LogInLayout(FloatLayout):
    def login_click(self, cc: str, pas: str) -> None:
        log = LogIn().Log(cc, pas)
        if log is not None:
            file = open('userinfo.config', 'w')
            file.write(f'{log.id};{log.mail};{log.full_name}')
            file.close()
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
    pass
