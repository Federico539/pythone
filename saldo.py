def saldo(saldo_inziale, tasso_interesse, numero_anni = None):
    saldo_finale = 0
    saldo_inziale = float(saldo_inziale)
    numero_anni = int(numero_anni)
    tasso_interesse = float(tasso_interesse)
    
    if numero_anni == None:
        for i in range(20):
            saldo_finale = saldo_inziale + (saldo_inziale * tasso_interesse)
            print(saldo_finale)
    else:
        for i in range(numero_anni):
            saldo_finale = saldo_inziale + (saldo_inziale * tasso_interesse)
        return saldo_finale

denaro = input("inserisci il denaro che vuoi mettere nel conto bancario: ")
tasso = input("Inserisci il tasso d' interesse annuo (in decimali): ")
anni = input("inserisci il numero di anni: ")

saldo_conto = saldo(denaro, tasso, anni)

print("il saldo del tuo conto bancario dopo",anni,"anni è",saldo_conto)