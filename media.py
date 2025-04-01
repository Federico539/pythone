i=0
somma=0
valore = ' '

while valore != 'exit':
    valore = input("inserisci un numero: ")
    if valore == 'exit':
        break
    somma += int(valore)
    i += 1

media = float(somma/i)
print('la media dei numeri inseriti è',media)