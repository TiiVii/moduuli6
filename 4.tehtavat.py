def lista(luvut):
    print('Luvut ovat: ')
    for l in luvut:
        print(f'- {int(l)}')
    return

luvut = [2,6,42,26]
lista(luvut)


print(f'Lukujen summa on: {sum(luvut)}.')