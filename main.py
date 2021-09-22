import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from settings_json import settings_json
from kivy.uix.image import Image

kivy.require('2.0.0')

# Set ratio
Window.size = (1920 / 2, 1080 / 2)


# Run fullscreen
# Window.fullscreen = 'auto'
# Or
# Window.fullscreen = True
# Window.borderless = False

# Custom
class ImageWithConfig(Image):
    def check_path_promo(self):
        self.source = App.get_running_app().config.get('Promo', 'promo_path')
        return self.source

    def check_path_bg(self):
        self.source = App.get_running_app().config.get('Main', 'bg_path')
        return self.source


class Interface(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        # Load config, remove default
        self.use_kivy_settings = False
        settings = self.config.items('Promo', 'Main')
        # Bind key action
        Window.bind(on_keyboard=self.key_action)
        return Interface()

    # Shortcut for settings
    def key_action(self, window, key, scancode, codepoint, modifier):
        if modifier == ['shift'] and codepoint == 'm':
            self.open_settings()

    # Custom settings
    def build_config(self, config):
        config.setdefaults('Promo', {
            'promo_path': '...',
        })
        config.setdefaults('Main', {
            'title_main': '',
            'bg_path': '...',
            'vk_link': 'vk.com/',
            'insta_link': 'instagram.com/'
        })

    def build_settings(self, settings):
        settings.add_json_panel('Settings',
                                self.config,
                                data=settings_json
                                )

    def on_config_change(self, config, section, key, value):
        self.root.ids.image_promo.check_path_promo()
        self.root.ids.image_bg.check_path_bg()


if __name__ == '__main__':
    MainApp().run()
