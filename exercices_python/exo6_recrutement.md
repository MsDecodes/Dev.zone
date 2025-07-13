
## 🔹 Exercice 6 — Recrutement : accès plateforme
### 🎯 Contexte :
Système de pré-filtrage à l’entrée d’une plateforme de recrutement.

### ✅ Règles :
- Moins de 18 ans → inscription interdite
- Pas de diplôme → refuser la candidature
- Diplômé :
  - plus de 2 ans d’expérience → senior
  - sinon → junior

### 🧠 Logique :
Enchaînement structuré de `if`, `elif`, `else`. Booléen `has_graduated`, vérification de l’expérience.