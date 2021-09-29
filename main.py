import kivy
import os, sys
import pathlib
import webbrowser
from kivy.config import Config

Config.set('kivy', 'window_icon', 'source/gob_icon.ico')
Config.set('graphics', 'window_state', 'maximized')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from settings_json import settings_json
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.resources import resource_add_path, resource_find

kivy.require('2.0.0')


def return_settings_json(key, value):
    result = App.get_running_app().config.get(key, value)
    return result


# Change Images
class ImageWithConfig(Image):

    def check_path_promo(self):
        self.source = return_settings_json('Promo', 'promo_path')
        return self.source

    def check_path_bg(self):
        self.source = return_settings_json('Main', 'bg_path')
        return self.source


# Change Title
class LabelWithConfig(Label):
    def check_title(self):
        self.text = return_settings_json('Main', 'title_main')
        return self.text


# Connect buttons to links
class SocialButton(Button):

    def __init__(self, **kwargs):
        super(SocialButton, self).__init__(**kwargs)
        self.instagram_link = return_settings_json('Main', 'insta_link')
        self.vkontakte_link = return_settings_json('Main', 'vk_link')
        self.discord_link = return_settings_json('Main', 'disc_link')

    def check_btn_inst(self):
        self.instagram_link = return_settings_json('Main', 'insta_link')

    def check_btn_vk(self):
        self.vkontakte_link = return_settings_json('Main', 'vk_link')

    def check_btn_disc(self):
        self.discord_link = return_settings_json('Main', 'disc_link')

    def open_link_inst(self):
        webbrowser.open(self.instagram_link)

    def open_link_vk(self):
        webbrowser.open(self.vkontakte_link)

    def open_link_disc(self):
        webbrowser.open(self.discord_link)


class Interface(BoxLayout):
    pass


class MainApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_path = pathlib.Path(__file__).parent.parent.resolve()

    def build(self):
        # Load config, remove default
        self.title = 'GoB Promo'
        self.use_kivy_settings = False
        self.config.items('Promo', 'Main')
        return Interface()

    # Custom settings
    def build_config(self, config):
        config.setdefaults('Promo', {
            'promo_path': 'source/promo_default.jpg',
        })
        config.setdefaults('Main', {
            'title_main': 'GoB Promotional title',
            'bg_path': 'source/background_default.jpg',
            'disc_link': 'https://discord.com',
            'insta_link': 'https://www.instagram.com',
            'vk_link': 'https://vk.com'
        })

    def build_settings(self, settings):
        settings.add_json_panel('Settings',
                                self.config,
                                data=settings_json
                                )

    def on_config_change(self, config, section, key, value):
        # Chek Global config change
        self.root.ids.image_promo.check_path_promo()
        self.root.ids.image_bg.check_path_bg()
        self.root.ids.title_main.check_title()
        self.root.ids.btn_inst.check_btn_inst()
        self.root.ids.btn_vk.check_btn_vk()
        self.root.ids.btn_disc.check_btn_disc()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run()
