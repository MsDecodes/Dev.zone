prenom = input("Quel est votre prénom?")
age = int(input("Quel est votre âge?"))
motif_visite = input("Quel est le motif de votre visite?").lower()
has_card = input("As-tu une carte d'accès physique valide? (oui/non)").lower() == "oui"
if age < 18:
    print (f"{prenom},vous ne pouvez pas entrer. Accès interdit aux mineurs.")
else:
    if not has_card:
        print (f"{prenom},vous devez être accompagné.e pour rentrer.")
    else:
        if motif_visite == "entretien":
            print (f"Bonne chance pour ton entretien, {prenom} !")
        elif motif_visite == "client":
            print (f"Bienvenue {prenom}, un chargé de compte va vous recevoir.")
        else:
            print (f"Merci pour votre visite, {prenom}.")



