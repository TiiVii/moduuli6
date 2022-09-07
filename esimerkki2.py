def tervehdi(teksti, kerrat):
    for i in range(kerrat):
        print(teksti)
    return

def tuumat_senteiks(tuumat):
    sentit = 2.54 * tuumat
    return sentit

tuumamaara = float(input('anna tuumamaamra: \n'))
senttimaara = tuumat_senteiks(tuumamaara)
print(f'{tuumamaara:.2f} tuumaa on {senttimaara:.2f} senttia')