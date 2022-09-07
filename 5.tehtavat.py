def lista(luvut):
    print('Lista on:')
    for i in luvut:
        print(f'-{int(i)}')
    return

luvut = [1,2,3,14,15,16,21]
lista(luvut)
print(f'Parilliset luvut listassa ovat: {[i for i in luvut if i % 2 == 0]}.')
