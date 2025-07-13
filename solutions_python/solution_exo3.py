age = int(input("Quel est votre âge?"))
is_vaccinated = input("Êtes-vous vacciné.e? (oui/non))").lower() == "oui"
if age < 16 :
    print ("Accès réfusé.")
else :
    if not is_vaccinated :
     print ("Accès réfusé.")
    else :
        if age < 25 :
            print ("Tarif jeune.")
        else :
            print ("Tarif standard.")
