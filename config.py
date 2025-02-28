import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration Dust
DUST_API_KEY = os.getenv('DUST_API_KEY')
DUST_WORKSPACE_ID = os.getenv('DUST_WORKSPACE_ID')

# Configuration Email
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT', 'frederic.denel@dadvisor.ai')

# Configuration SMTP
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')  # Exemple avec Gmail
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))

# Configuration de l'application
QUERY_TEXT = os.getenv('QUERY_TEXT', "Fais-moi un résumé des opportunités d'investissement actuelles")
SCHEDULE_TIME = os.getenv('SCHEDULE_TIME', "08:00")  # Heure d'envoi quotidien
