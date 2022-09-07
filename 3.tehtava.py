def operaatio():
    while True:
        gallon = float(input('Anna gallonamaara: '))
        muunnos = gallon * 3.785412
        if gallon <0:
            return
        print(f'{muunnos:.2f}')
operaatio()