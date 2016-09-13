#!/usr/bin/python3
import notify2, pyperclip
from translate import translate

text = pyperclip.paste()

translated_text = translate({
    "from": None,
    "to": "ru",
    "text": text,
    #--------------------
    "method": "google",
    #--------------------
    # "method": "yandex",
    # "method_options": {
    #     "api_key": "",
    # }
    #--------------------
})

# print('Translated text: "{}"'.format(translated_text))

notify2.init('translate_selection')
notify2.Notification('Translated text', translated_text).show()
