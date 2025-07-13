🚀 Démarrage rapide – Travailler avec Git et GitHub en local
Ce guide résume les manipulations essentielles pour créer un projet localement avec Git, l’organiser, le versionner et le publier sur GitHub.

📁 1. Créer un projet local
cd ~/Documents
mkdir nom_du_projet
cd nom_du_projet
Remplace nom_du_projet par le nom réel (ex: exercices_python, solutions_python, etc.)

📝 2. Créer des fichiers ou dossiers
touch fichier.py           # Créer un fichier
mkdir dossier_supplement   # Créer un dossier
mv ancien.py nouveau.py    # Renommer un fichier
rm fichier.py              # Supprimer un fichier

🧠 3. Initialiser Git
git init

🟢 4. Suivre les fichiers avec Git
git status                     # Voir les fichiers modifiés
git add .                      # Ajouter tous les fichiers
git add nom_fichier            # Ajouter un fichier précis

💬 5. Commit (enregistrer un état du projet)
git commit -m "Message clair sur les modifications"

🌐 6. Lier à GitHub (une seule fois)
git remote add origin https://github.com/TONUTILISATEUR/NOM_DU_REPO.git
Tu peux retrouver cette URL sur la page de ton repo GitHub.

⬆️ 7. Envoyer sur GitHub
git push -u origin main
✨ Bonnes pratiques
Utilise des noms clairs et cohérents pour tes dossiers (exercices_python, solutions_python, etc.)

Commence toujours par un README.md clair pour expliquer le contexte.

Utilise des commits fréquents et explicites ("Ajout exo1", "Correction logique exo3", etc.)

🧰 Bonus : commandes utiles
ls                  # Lister les fichiers d'un dossier
pwd                 # Afficher le chemin courant
code .              # Ouvrir le projet dans VS Code (si installé)
clear               # Nettoyer le terminal