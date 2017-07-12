#!/usr/bin/python3
import notify2, pyperclip
from translate import translate
import subprocess
from sys import platform

if platform in ["linux", "linux2"]:
    subprocess.call("xclip -out -selection primary | xclip -in -selection clipboard", shell=True)

text = pyperclip.paste().replace("\n", " ")

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

pyperclip.copy(translated_text)

notify2.init('translate_selection')
notify2.Notification('Translated text', translated_text).show()

