# Investment Analyst Bot

Ce bot interroge quotidiennement l'assistant @SeniorAnalyst via l'API Dust et envoie les analyses par email.

## Configuration

1. Copiez le fichier `.env.example` en `.env`
2. Remplissez les variables d'environnement dans le fichier `.env`

## Installation

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
