def calcolaMedia(myFile):
    somma = 0
    count = 0

    for line in myFile:
        somma += float(line.strip())
        count += 1

    if count == 0:
        return 0
    
    return somma / count

def trovaMassimo(myFile):
    numeroMassimo = float('-inf')

    for line in myFile:
        if(float(line) > numeroMassimo):
            numeroMassimo = float(line)
    
    return numeroMassimo




fileName = input("inserisci il nome del file: ")

try:
    with open(fileName, "r") as apriFile:
        media = calcolaMedia(apriFile)
    
    with open(fileName, "r") as apriFile:
        massimo = trovaMassimo(apriFile)

    print("La media dei numeri contenuti nel file è: ", media)
    print("Il massimo dei numeri contenuti nel file è: ", massimo)

except:
    print("ERRORE: il file che hai chiesto non è stato trovato")

finally:
    newFile.close()
