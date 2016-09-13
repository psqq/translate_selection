import urllib.request
import urllib.parse
import xml.etree.ElementTree as etree


def translate(text, to_lang, from_lang=None, api_key=None):
    if api_key is None:
        return "Error: no api key!"
    if from_lang is None:
        lang = to_lang
    else:
        lang = from_lang + "-" + to_lang
    args = "key={}&lang={}&text={}".format(api_key, lang, urllib.parse.quote(text))
    link = "https://translate.yandex.net/api/v1.5/tr/translate?" + args
    request = urllib.request.Request(link, method="POST")
    xml = urllib.request.urlopen(request).read().decode("utf-8")
    tree = etree.fromstring(xml)
    return tree.find('text').text


if __name__ == '__main__':
    key = ""
    print(translate('Hola como estas?', 'ru', api_key=key))
    print(translate('Hola como estas?', 'en', api_key=key))

