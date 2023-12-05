from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.app import App


class ProfileScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass

    def show(self) -> None:
        self.ids.name_profile.text = f'{App.get_running_app().usr.full_name}'
        self.ids.mail_profile.text = f'{App.get_running_app().usr.mail}'
        self.ids.id_profile.text = f'ID: {App.get_running_app().usr.id}'

    def end_sesion(self) -> None:
        app = App.get_running_app()
        app.usr.__init__()
        app.regis.__init__()
        app.alerts.__init__()
        app.crops.__init__()
        app.loginManager.__init__()
        app.statsManager.__init__()
        app.cropsManager.__init__()
        self.parent.parent.parent.switch_content("default")
        self.parent.parent.parent.parent.pop_to_label('login', 'cerrarsesion')


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


class BgCanvas(Widget):
    pass


Builder.load_file('profilescreen.kv')
