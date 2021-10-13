import json

settings_json = json.dumps([
    {
        'type': 'title',
        'title': 'Promo'

    },
    {
        'type': 'path',
        'title': 'Promo picture',
        'desc': 'Choose promotional picture',
        'section': 'Promo',
        'key': 'promo_path'
    },
    {
        'type': 'title',
        'title': 'Main'

    },
    {
        'type': 'string',
        'title': 'Title',
        'desc': 'Shortly describe your promotional offer',
        'section': 'Main',
        'key': 'title_main'
    },
    {
        'type': 'path',
        'title': 'Background picture',
        'desc': 'Choose background image',
        'section': 'Main',
        'key': 'bg_path'
    },
    {
        'type': 'title',
        'title': 'Buttons'
    },
    {
        'type': 'string',
        'title': 'Yandex',
        'desc': 'Insert link to Yandex',
        'section': 'Buttons',
        'key': 'yandex_link'
    },
    {
        'type': 'bool',
        'title': 'Visible',
        # 'desc': 'turn off button',
        'section': 'Buttons',
        'key': 'yandex_hide'
    },
    {
        'type': 'string',
        'title': '2GIS',
        'desc': 'Insert link to 2GIS',
        'section': 'Buttons',
        'key': 'twogis_link'
    },
    {
        'type': 'bool',
        'title': 'Visible',
        # 'desc': 'turn off button',
        'section': 'Buttons',
        'key': 'twogis_hide'
    },
    {
        'type': 'string',
        'title': 'Instagram',
        'desc': 'Insert link to Instagram page',
        'section': 'Buttons',
        'key': 'insta_link'
    },
    {
        'type': 'bool',
        'title': 'Visible',
        # 'desc': 'turn off button',
        'section': 'Buttons',
        'key': 'insta_hide'
    },
    {
        'type': 'string',
        'title': 'VKontakte',
        'desc': 'Insert link to VKontakte page',
        'section': 'Buttons',
        'key': 'vk_link'
    },
    {
        'type': 'bool',
        'title': 'Visible',
        # 'desc': 'turn off button',
        'section': 'Buttons',
        'key': 'vk_hide'
    },

])
