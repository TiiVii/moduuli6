def tuumatstasenttiin():
    global sentit
    sentit = 2.54 * tuumat
    return
tuumat = float(input('anna maara: '))
sentit = 0.0
tuumatstasenttiin()
print(f'{tuumat:.2f} tuumaa on {sentit:.2f} senttia.')