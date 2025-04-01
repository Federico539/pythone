reddito_str = input("inserisci il tuo reddito annuo: ")
reddito = float(reddito_str)

if reddito <= 28000:
    tasse = reddito * 0.23
elif reddito > 28000 and reddito <= 50000:
    tasse = reddito * 0.35
else:
    tasse = reddito * 0.43

print("paghi",tasse,"euro di tasse all'anno")