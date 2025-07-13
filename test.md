Créer un projet Git proprement (terminal)
1️⃣ Créer un dossier de projet
mkdir mon-projet
cd mon-projet

2️⃣ Créer des fichiers dedans
touch README.md
touch xx.py

3️⃣ Initialiser un dépôt Git
git init

4️⃣ Voir l’état des fichiers
git status

5️⃣ Ajouter les fichiers au suivi Git
git add .

6️⃣ Faire un commit (photo de l'état actuel)
git commit -m "Initial commit"

7️⃣ Lier le dépôt local à GitHub
(dépôt déjà créé sur GitHub au préalable)
git remote add origin https://github.com/username/mon-projet.git

8️⃣ Envoyer les fichiers sur GitHub
git push -u origin main
✏️ Autres commandes très utiles
Renommer un fichier :
mv ancien.py nouveau.py

Supprimer un fichier :
rm fichier.py

Supprimer un dossier :
rm -r nom_du_dossier

Créer un sous-dossier :
mkdir nom_du_sous_dossier

Déplacer un fichier dans un dossier :
mv mon_script.py dossier/

🔄 Mise à jour après modification
Quand tu modifies un fichier :
git status           # Vérifie ce qui a changé
git add .            # Ajoute les changements
git commit -m "Message clair"
git push             # Envoie sur GitHub