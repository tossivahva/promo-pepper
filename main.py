import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from settings_json import settings_json

kivy.require('2.0.0')

# Set ratio
Window.size = (1920 / 2, 1080 / 2)


# Run fullscreen
# Window.fullscreen = 'auto'
# Or
# Window.fullscreen = True
# Window.borderless = False


class Interface(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        Window.bind(on_keyboard=self.key_action)
        return Interface()

    # Shortcut for settings
    def key_action(self, window, key, scancode, codepoint, modifier):
        if modifier == ['shift'] and codepoint == 'm':
            self.open_settings()

    # Custom settings
    def build_config(self, config):
        config.setdefaults('promo', {
            'path': '/images/'})

    def build_settings(self, settings):
        settings.add_json_panel('General',
                                self.config,
                                data=settings_json
                                )

    def on_config_change(self, config, section, key, value):
        pass


if __name__ == '__main__':
    MainApp().run()
