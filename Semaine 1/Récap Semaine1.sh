🧾 Récapitulatif – Semaine 1 | Fondamentaux Python + Git

🐍 Partie 1 – Python : Logique, conditions et structures de base

🎯 Objectif :
Apprendre à coder des scripts simples basés sur des conditions logiques, des inputs utilisateurs, et structurer proprement son raisonnement.

🔸 1. Les fonctions de base apprises
input() → Sert à demander une information à l’utilisateur. Toujours de type str par défaut.

int() → Sert à convertir une string en entier, souvent utilisé avec un input().

print() → Sert à afficher un message dans la console.

f"{}" → C’est du f-string. Formatage de chaînes : on insère directement des variables dans du texte.

if / elif / else → Structure conditionnelle de base :

if teste une condition

elif teste une autre si la première est fausse

else exécute un bloc si aucune condition n'est vraie

🔸 2. Les types logiques utilisés
booléens (True / False) : utilisés pour tester des états (ex: has_card, is_vaccinated, has_graduated)

opérateurs logiques :

== égal à

!= différent

> / < sup / inf

and, or, not pour combiner des conditions

🔸 3. Exercices codés et logiques appliquées
Exercice	Thème	Compétences visées
exo1-majorite	Âge : enfant, ado, adulte	conditions simples
exo2-batiment	Accès selon âge + carte + motif	conditions imbriquées + input().lower()
exo3-club	Accès selon âge + vaccination	imbriqué + booléens
exo4-tarif	Tarification avec and / or	booléens + logique combinée
exo5-teletravail	Éligibilité au télétravail	test conditionnel rigoureux
exo6-recrutement	Recrutement plateforme	test d’âge + expérience + diplôme

Tous ces scripts sont dans exercices_python/ et leurs solutions dans solutions_python/, bien organisés dans le dossier semaine_1.

🧰 Partie 2 – Git & GitHub : Maîtrise du workflow de base
🎯 Objectif :
Savoir initialiser un dépôt Git, suivre l'évolution du code, et le synchroniser avec GitHub.

🔸 Workflow Git local complet
bash
Copier
Modifier
cd Documents  # Aller dans le bon répertoire
mkdir nom_du_projet
cd nom_du_projet
git init                       # Initialiser git
touch fichier.py               # Créer un fichier
git status                     # Vérifier les fichiers modifiés
git add fichier.py             # Ajouter les fichiers au staging
git commit -m "Mon commit"     # Valider les modifications
git remote add origin https://github.com/...  # Lier au repo GitHub
git push -u origin main        # Pousser le code vers GitHub

🔸 Commandes utiles
Action	Commande
Créer dossier	mkdir nom
Supprimer fichier	rm nom
Renommer fichier/dossier	mv ancien nouveau
Lister contenu	ls
Se déplacer	cd nom_dossier ou cd ..
Créer fichier	touch nom.py ou nano nom.py
Voir l’historique Git	git log
