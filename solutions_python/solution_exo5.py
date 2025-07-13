anciennete = int(input("Quel est votre votre ancienneté dans l'entreprise? (En mois)"))
is_contracted = input("Etes vous en CDI?").lower() == "oui"
if anciennete >= 12 and is_contracted:
    print("Vous êtes éligible au télétravail.")
else:
    print("Vous n'êtes pas éligible au télétravail.")
