import kivy
from kivy.config import Config
# Icon
Config.set('kivy', 'window_icon', 'images/ico/gob-icn.ico')

import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from settings_json import settings_json
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('2.0.0')

# Set ratio
Window.size = (1920, 1080)

# Run fullscreen
Window.maximize()


# Change Images
class ImageWithConfig(Image):
    def check_path_promo(self):
        self.source = App.get_running_app().config.get('Promo', 'promo_path')
        return self.source

    def check_path_bg(self):
        self.source = App.get_running_app().config.get('Main', 'bg_path')
        return self.source


# Change Title
class LabelWithConfig(Label):
    def check_title(self):
        self.text = App.get_running_app().config.get('Main', 'title_main')
        return self.text


# Connect buttons to links
class SocialButton(Button):

    def __init__(self, **kwargs):
        super(SocialButton, self).__init__(**kwargs)
        self.instagram_link = App.get_running_app().config.get('Main', 'insta_link')
        self.vkontakte_link = App.get_running_app().config.get('Main', 'vk_link')

    def check_btn_inst(self):
        self.instagram_link = App.get_running_app().config.get('Main', 'insta_link')

    def check_btn_vk(self):
        self.vkontakte_link = App.get_running_app().config.get('Main', 'vk_link')

    def open_link_inst(self):
        webbrowser.open(self.instagram_link)

    def open_link_vk(self):
        webbrowser.open(self.vkontakte_link)


class Interface(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        # Load config, remove default
        self.title = 'GoB Promo'
        self.use_kivy_settings = False
        self.config.items('Promo', 'Main')
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
            'insta_link': 'instagram.com/',
            'vk_link': 'vk.com/'
        })

    def build_settings(self, settings):
        settings.add_json_panel('Settings',
                                self.config,
                                data=settings_json
                                )

    def on_config_change(self, config, section, key, value):
        # Chek data on config change
        self.root.ids.image_promo.check_path_promo()
        self.root.ids.image_bg.check_path_bg()
        self.root.ids.title_main.check_title()
        self.root.ids.btn_inst.check_btn_inst()
        self.root.ids.btn_vk.check_btn_vk()


if __name__ == '__main__':
    MainApp().run()
