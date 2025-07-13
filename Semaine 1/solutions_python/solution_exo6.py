age = int(input("Quel est votre âge?"))
has_graduated = input("Avez-vous un diplôme?").lower() == "oui"
experience = int((input("Combien d'années d'expérience avez-vous?")))
if age < 18 :
    print ("Inscription interdite")
elif not has_graduated :
    print ("Vous devez d’abord obtenir un diplôme pour postuler.")
else :
    if experience > 2 :
        print ("Vous avez un profil senior")
    else:
        print ("Profil junior enregistré ")
