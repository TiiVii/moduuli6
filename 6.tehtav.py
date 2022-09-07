pizza1ha = float(input('Anna ensimmaisen pizzan halkaisija: '))
pizza1hi = float(input('Anna ensimmaisen pizzan hinta: '))
pizza2ha = float(input('Anna toisen pizzan halkaisija: '))
pizza2hi = float(input('Anna toisen pizzan hinta: '))

from math import pi

def pizzataikina():
    arvo2 = pizza2hi / ((pi * ((pizza2ha/2)) / 100) ** 2)
    arvo1 = pizza1hi / ((pi * ((pizza1ha/2)) / 100) ** 2)
    if arvo1 < arvo2:
        print('Ensimmainen pizza antaa rahallisesti paremman vastineen.')
    if arvo1 > arvo2:
        print('Toinen pizza antaa rahallisesti paremman vastineen.')
    return
pizzataikina()