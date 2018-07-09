import urllib.request
import json


def getpage(title):
    url = 'https://pl.wikipedia.org/w/api.php'
    values = {
	"action": "query",
	"format": "json",
	"list": "embeddedin",
	"formatversion": "2",
	"eititle": title,
	"eilimit": "500"
}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    bajty = response.read()
    stringi = bajty.decode('utf-8')
    slowniczek = json.loads(stringi)
    content = slowniczek['query']['embeddedin']
    return content



def nadpiszPlik(plik, strona):
    text_file = open(plik, "a", encoding='utf-8')
    text_file.write(strona)
    text_file.close()

for i in getpage("Szablon:POL_miasto_infobox"):
    nazwaArtykulu = i['title']
    nadpiszPlik('listaLinkujacych.txt', nazwaArtykulu+'\n')