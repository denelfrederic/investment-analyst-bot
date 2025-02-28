import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import logging
import os
from dotenv import load_dotenv
from config import *

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("investment_bot.log"),
        logging.StreamHandler()
    ]
)

def query_senior_analyst():
    """Interroge @SeniorAnalyst via l'API Dust"""
    logging.info("Interrogation de @SeniorAnalyst...")
    
    headers = {
        "Authorization": f"Bearer {DUST_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Création d'une nouvelle conversation
    conversation_endpoint = f"https://dust.tt/api/v1/w/{DUST_WORKSPACE_ID}/assistant/conversations"
    
    conversation_payload = {
        "message": {
            "content": QUERY_TEXT
        },
        "mentions": [
            {
                "configurationId": "SeniorAnalyst"  # Identifiant de l'assistant
            }
        ],
        "blocking": True  # Attendre la réponse complète
    }
    
    try:
        # Créer une conversation
        conversation_response = requests.post(
            conversation_endpoint, 
            json=conversation_payload, 
            headers=headers
        )
        conversation_response.raise_for_status()
        
        conversation_data = conversation_response.json()
        logging.info(f"Réponse reçue")
        
        # Extraire la réponse de l'assistant
        if 'conversation' in conversation_data and 'content' in conversation_data['conversation']:
            for message in conversation_data['conversation']['content']:
                if message.get('role') == 'assistant':
                    return message.get('content')
        
        logging.warning("Format de réponse inattendu")
        return None
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Erreur lors de la requête à Dust: {e}")
        return None

def send_email(content):
    """Envoie l'analyse par email"""
    logging.info(f"Envoi de l'email à {EMAIL_RECIPIENT}...")
    
    msg = MIMEMultipart()
    msg['Subject'] = f"📊 Analyse d'investissement du {datetime.now().strftime('%d/%m/%Y')}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT
    
    # Formatage du contenu
    formatted_content = f"""
    Bonjour,
    
    Voici l'analyse d'investissement quotidienne générée par @SeniorAnalyst.
    
    Date: {datetime.now().strftime('%d/%m/%Y')}
    
    {content}
    
    Cordialement,
    Votre assistant d'investissement automatisé
    """
    
    msg.attach(MIMEText(formatted_content, 'plain'))
    
    try:
        # Configuration du serveur SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info("Email envoyé avec succès")
            return True
    except Exception as e:
        logging.error(f"Erreur lors de l'envoi de l'email: {e}")
        return False

def daily_job():
    """Tâche quotidienne : interroger @SeniorAnalyst et envoyer l'email"""
    logging.info(f"Exécution de la tâche quotidienne - {datetime.now()}")
    
    # Interroger @SeniorAnalyst
    analysis = query_senior_analyst()
    
    if analysis:
        # Envoyer l'email
        send_email(analysis)
    else:
        logging.error("Aucune analyse reçue")

def main():
    """Fonction principale"""
    logging.info("Démarrage du bot d'analyse d'investissement...")
    
    # Planification de la tâche quotidienne
    schedule.every().day.at(SCHEDULE_TIME).do(daily_job)
    logging.info(f"Tâche planifiée tous les jours à {SCHEDULE_TIME}")
    
    # Boucle principale
    while True:
        schedule.run_pending()
        time.sleep(60)  # Vérifier toutes les minutes

if __name__ == "__main__":
    main()
