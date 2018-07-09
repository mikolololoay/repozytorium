def zapiszDoNotatnika(plik, strona):
    text_file = open(plik, "w")
    text_file.write(strona)
    text_file.close()

def wczytajNazwy(plik):
    text_file = open(plik, "r")
    alist = text_file.read().splitlines()
    text_file.close()
    return alist


nazwyStron = wczytajNazwy('pliki.txt')
n=0
for i in nazwyStron:
    g=str(i.encode('utf-8'))
    zapiszDoNotatnika('zapisane'+str(n)+'.txt',getpage(g))
    n=n+1