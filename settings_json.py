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
        'type': 'string',
        'title': 'Instagram',
        'desc': 'Insert link to Instagram page',
        'section': 'Main',
        'key': 'insta_link'
    },
    {
        'type': 'string',
        'title': 'VKontakte',
        'desc': 'Insert link to VKontakte page',
        'section': 'Main',
        'key': 'vk_link'
    },

])
