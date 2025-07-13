## 🔹 Exercice 3 — Club de sport : tarif selon âge & vaccination
### 🎯 Contexte :
Filtrage à l’entrée d’un club sportif.

### ✅ Règles :
- Moins de 16 ans → accès refusé
- 16 ans ou plus :
  - non vacciné → refusé
  - vacciné :
    - moins de 25 ans → tarif jeune
    - sinon → tarif standard

### 🧠 Logique :
Conditions imbriquées. Utilisation d’un booléen `is_vaccinated`.
