max = 0
numero = 0
count = 0

while numero >= 0:
    numero = int(input("inserisci un numero intero positivo:"))
    if numero >= 0:
        count = count + 1
        if numero > max:
            max = numero
            

if count > 0:
    print("il numero massimo tra quelli inseriti è",max)
else:
    print("nessun numero massimo trovato")