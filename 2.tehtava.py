from random import randint

lkm = int(input('Anna nopan maksimisilmaluku: '))

def heitto():
    while True:
        noppa = randint(1, lkm)
        print(noppa)
        if noppa ==lkm:
            return
heitto()