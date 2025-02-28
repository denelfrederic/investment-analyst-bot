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




# Documentation du Bot d'Analyse d'Investissement

## 1. Connexion au serveur
```bash
ssh root@srv731888.hstgr.cloud
```

## 2. Navigation vers le projet
```bash
cd /apps/investment-bot
```

## 3. Vérification du service
```bash
# Voir l'état du service
sudo systemctl status investment-bot.service

# Voir les logs en temps réel
sudo journalctl -u investment-bot.service -f
# (Ctrl + C pour quitter les logs)

# Voir les logs du bot
tail -f /apps/investment-bot/investment_bot.log
```

## 4. Commandes de gestion du service
```bash
# Démarrer le service
sudo systemctl start investment-bot.service

# Arrêter le service
sudo systemctl stop investment-bot.service

# Redémarrer le service
sudo systemctl restart investment-bot.service
```

## 5. Test manuel d'envoi d'email
```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Exécuter le job manuellement
python -c "from main import daily_job; daily_job()"
```

## 6. Configuration
- Fichier de configuration : `.env`
- Service systemd : `/etc/systemd/system/investment-bot.service`
- Logs : `/apps/investment-bot/investment_bot.log`

## 7. Horaire d'exécution
- Le bot s'exécute automatiquement chaque jour à 8h00
- Les résultats sont envoyés à frederic.denel@dadvisor.ai

## 8. En cas de problème
1. Vérifier les logs du service
2. S'assurer que le fichier .env est correctement configuré
3. Vérifier que le service est actif
4. Tester l'envoi manuel d'email

Voulez-vous que je détaille l'une de ces sections en particulier ?
