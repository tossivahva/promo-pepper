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
        self.insta_link = return_settings_json('Buttons', 'insta_link')
        self.vk_link = return_settings_json('Buttons', 'vk_link')
        self.yandex_link = return_settings_json('Buttons', 'yandex_link')
        self.twogis_link = return_settings_json('Buttons', 'twogis_link')

    def hide_btn(self, key, value):
        self.value = value
        self.value = return_settings_json(key, value)
        if self.value == '1':
            self.opacity = 1
            self.disabled = False
            self.size_hint_x = 1
        if self.value == '0':
            self.opacity = 0
            self.disabled = True
            self.size_hint_x = 0.01
        return [self.opacity, self.disabled, self.size_hint_x]

    def check_btn_insta(self):
        self.insta_link = return_settings_json('Buttons', 'insta_link')

    def check_btn_vk(self):
        self.vk_link = return_settings_json('Buttons', 'vk_link')

    def check_btn_yandex(self):
        self.yandex_link = return_settings_json('Buttons', 'yandex_link')

    def check_btn_twogis(self):
        self.twogis_link = return_settings_json('Buttons', 'twogis_link')

    def open_link(self, url):
        self.url = url
        webbrowser.open(self.url)


class Interface(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        # Load config, remove default
        self.title = 'GoB Promo'
        self.use_kivy_settings = False
        return Interface()

    # Custom settings
    def build_config(self, config):
        config.setdefaults('Promo', {
            'promo_path': 'source/promo_default.jpg',
        })
        config.setdefaults('Main', {
            'title_main': 'GoB Promotional title',
            'bg_path': 'source/background_default.jpg',

        })
        config.setdefaults('Buttons', {
            'yandex_link': 'https://yandex.com',
            'yandex_hide': True,
            'insta_link': 'https://www.instagram.com',
            'insta_hide': True,
            'vk_link': 'https://vk.com',
            'vk_hide': True,
            'twogis_link': 'https://2gis.com',
            'twogis_hide': True,
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
        # Check btn link value
        self.root.ids.btn_vk.check_btn_vk()
        self.root.ids.btn_yandex.check_btn_yandex()
        self.root.ids.btn_twogis.check_btn_twogis()
        self.root.ids.btn_insta.check_btn_insta()
        # Hide toggle
        self.root.ids.btn_yandex.hide_btn('Buttons', 'yandex_hide')
        self.root.ids.btn_twogis.hide_btn('Buttons', 'twogis_hide')
        self.root.ids.btn_insta.hide_btn('Buttons', 'insta_hide')
        self.root.ids.btn_vk.hide_btn('Buttons', 'vk_hide')


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run()
