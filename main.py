import kivy
from kivy.app import App
from kivy.uix.widget import Widget

kivy.require('2.0.0')


class Front(Widget):
    pass


class MainApp(App):

    def build(self):
        return Front()


if __name__ == '__main__':
    MainApp().run()
