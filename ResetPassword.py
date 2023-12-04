from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import re

class ResetScreen(FloatLayout):

    def equals(self) -> bool:
        return self.ids.NewPassword.text == self.ids.ConfirmPassword.text

    def validate_len(self) -> bool:
        return True if len(self.ids.NewPassword.text) >= 8 else False

    def validate_special(self) -> bool:
        return bool(re.compile(r'[!@#$%^&*()_+={}\[\]:;<>,.?/~`\\|-]').search(self.ids.NewPassword.text))

    def check(self) -> bool:
        if self.equals():
            if self.validate_len():
                if self.validate_special():
                    return True
                else:
                    self.ids.message.text = "La contraseña debe contener caracteres especiales ASCII"
            else:
                self.ids.message.text = "La contraseña debe ser de 8 carateres minimo"
        else:
            self.ids.message.text = "Las contraseñas no coinciden"
        return False

    def rst(self) -> None:
        if self.check():
            App.get_running_app().loginManager.changePassw(App.get_running_app().usr.id, self.ids.NewPassword.text)
            self.parent.parent.push("Correct_reset")


class BackgroundColor(Widget):
    pass


class BgLabel(Label, BackgroundColor):
    pass


Builder.load_file('resetsrcreen.kv')
