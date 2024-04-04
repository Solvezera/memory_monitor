import os
import time
import psutil
from dotenv import load_dotenv
from twilio.rest import Client

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')

# Função para enviar SMS
def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=RECIPIENT_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

# Função para monitorar o uso de memória
def monitor_memory_usage():
    while True:
        mem_usage = psutil.virtual_memory().percent
        if mem_usage > 50:
            message = f'O uso de memória está em {mem_usage}% e ultrapassou 50%'
            send_sms(message)
            time.sleep(60)  # Espera 1 minuto antes de enviar outro alerta
        time.sleep(10)  # Verifica o uso de memória a cada 10 segundos

if __name__ == "__main__":
    monitor_memory_usage()
