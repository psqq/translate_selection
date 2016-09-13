import urllib.request
import urllib.parse


agent = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}


def translate(text, to_lang="auto", from_lang="auto"):
    if to_lang == None:
        to_lang = "auto"
    if from_lang == None:
        from_lang = "auto"
    before_trans = 'class="t0">'
    args = "hl={}&sl={}&q={}".format(to_lang, from_lang, urllib.parse.quote(text))
    link = "http://translate.google.com/m?" + args
    request = urllib.request.Request(link, headers=agent)
    page = urllib.request.urlopen(request).read().decode("utf-8")
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return(result)


if __name__ == '__main__':
    to_translate = 'Hola como estas?'
    print("%s >> %s" % (to_translate, translate(to_translate)))
    print("%s >> %s" % (to_translate, translate(to_translate, 'fr')))
    print("%s >> %s" % (to_translate, translate(to_translate, 'ru')))
