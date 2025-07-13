prenom = input("Quel est votre prénom?")
age = int(input("Quel est votre âge?"))
is_local_resident = input("Est-vous un résident local? (oui/non)").lower() == "oui"
has_student_card = input ("Avez-vous une carte étudiant? (oui/non)").lower() == "oui"
if age < 12 :
    print(f"{prenom}, votre entrée est gratuite.")
else:
    if 12 <= age <= 17:
        print(f"{prenom}, votre tarif est réduit.")
    else :
        if age >= 18 and has_student_card and is_local_resident :
            print (f"{prenom}, votre tarif est super réduit.")
        elif age >= 18 and (has_student_card or is_local_resident):
            print (f"{prenom}, votre tarif est réduit.")
        else:
            print (f"{prenom}, vous bénéficiez d'un tarif plein.")
