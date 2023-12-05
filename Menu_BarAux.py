from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import ProfileScreen, AlertScreen, HomeScreen, SearchScreen, AnalysisScreen, GraphicScreen, VersionScreen, AlertsMore, DefaultScreen


class ContentScreen(Screen):

    def __init__(self, content_widgets=None, **kwargs):
        super(ContentScreen, self).__init__(**kwargs)

        # Verifica si se proporcionó la lista de widgets
        if content_widgets:
            for widget in content_widgets:
                self.add_widget(widget)


class SecondScreen(Screen):
    def switch_content(self, tab_name):
        # Cambiar al contenido de la pestaña especificada
        self.ids.content_manager.current = tab_name

    def handle_touch(self, label_name, tab_name, *args):
        #cambiar el contenido de al presionar un label
        self.ids.content_manager.current = tab_name



class MenuBar(BoxLayout):
    pass


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


Builder.load_file('secondscreen.kv')
Builder.load_file('menubar.kv')
