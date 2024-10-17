import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import NumericProperty

class MainScreenManager(ScreenManager):
    user_progress = NumericProperty(0)
    password_progress = NumericProperty(0)

class MainApp(App):
    def build(self):
        return MainScreenManager()

if __name__ == '__main__':
    MainApp().run()