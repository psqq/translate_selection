import google, yandex


def translate(kw):
    text = kw['text']
    to = kw['to']
    _from = kw['from']
    method = kw['method']
    if method == 'google':
        return google.translate(text, to, _from)
    elif method == 'yandex':
        return yandex.translate(text, to, _from, kw['method_options']['api_key'])
    return "Error: Unknow method!"

