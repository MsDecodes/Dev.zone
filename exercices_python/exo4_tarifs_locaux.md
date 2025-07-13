## 🔹 Exercice 4 — Tarification spéciale (local/étudiant)
### 🎯 Contexte :
Gestion des tarifs selon l’âge, la résidence et le statut étudiant.

### ✅ Règles :
- Moins de 12 ans → gratuit
- 12 à 17 ans → tarif réduit
- 18 ans ou plus :
  - étudiant ET résident local → super réduit
  - étudiant OU résident → réduit
  - sinon → plein tarif

### 🧠 Logique :
Combinaison logique avec `and` et `or`. Utilisation de booléens `has_student_card`, `is_local_resident`.
