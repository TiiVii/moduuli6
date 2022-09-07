def inventaario(tavarat):
    print('sinulla on: ')
    for t in tavarat:
        print('-' + t)
    tavarat.clear()
    return


reppu = ['vesipullo', 'kartta', 'kompassi']
inventaario(reppu)
reppu.append('linkkuveitsi')
inventaario(reppu)