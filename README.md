---
title: SunuDiag
emoji: 🩺
colorFrom: blue
colorTo: green
sdk: docker
app_port: 10000
---

# 🩺 SunuDiag - Pré-diagnostic du paludisme

## Description

SunuDiag est une application web de pré-diagnostic du paludisme basée sur un modèle RandomForest entraîné sur le jeu de données **DataSANTE-221** (10 000 patients synthétiques).

L'application permet aux agents de santé de saisir les paramètres d'un patient (âge, température, glycémie, hémoglobine, saison) et d'obtenir une probabilité de paludisme avec un pré-diagnostic coloré.

## 🚀 URL en ligne

🔗 [https://sunudiag.onrender.com](https://sunudiag.onrender.com)

## 📊 Stack technique

| Composant | Technologie |
|-----------|-------------|
| Backend | FastAPI + Uvicorn |
| Frontend | HTML + Tailwind CSS |
| Modèle | Scikit-learn (RandomForest) |
| Conteneurisation | Docker |
| Déploiement | Render.com |

## 📋 Fonctionnalités

- ✅ Formulaire intuitif avec valeurs de référence
- ✅ Prédiction en temps réel via API REST
- ✅ Résultat coloré avec barre de progression
- ✅ Gestion des erreurs (données invalides, API hors ligne)
- ✅ Interface responsive (mobile/tablette/desktop)
- ✅ Avertissement santé visible

## 👤 Auteur

**Libasse Gassama**
- Master 1 IABD - DMI/FST/UCAD
- Université Cheikh Anta Diop de Dakar

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE)

## ⚠️ Avertissement

> **SunuDiag est un outil pédagogique de pré-diagnostic.**
> Il ne remplace jamais l'avis d'un professionnel de santé.
> En cas de doute, consultez un médecin.

## 🔧 Installation locale

```bash
# Cloner le projet
git clone https://github.com/LibasseGassama/sunudiag.git
cd sunudiag

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'API
uvicorn api.main:app --host 0.0.0.0 --port 7860


---

## 📁 5. Fichier : `Dockerfile` (pour Render)

**Vérifie que ton `Dockerfile` est comme ceci :**

```dockerfile
# L'image de depart : un Linux minimal avec Python 3.11
FROM python:3.11-slim

# Le repertoire de travail a l'interieur du conteneur
WORKDIR /app

# Installer les dependances AVANT de copier le code (cache Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le projet : API, frontend et modele
COPY api/ ./api/
COPY frontend/ ./frontend/
COPY models/ ./models/

# Port 10000 pour Render.com
EXPOSE 10000

# La commande lancee au demarrage du conteneur
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "10000"]