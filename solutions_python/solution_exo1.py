prenom = input("Quel est ton prénom?")
age = int(input("Quel est ton âge?"))

if age < 12:
    print(f"{prenom},tu es un enfant")
elif age < 18:
    print(f"{prenom},tu es un ado")
else:
    print(f"{prenom}, tu es un adulte")