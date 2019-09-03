from django.core.mail import EmailMessage
from datetime import datetime
import logging

def scheduledEmail():
    try:
        now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        logging.debug(now)
        email = EmailMessage('Scheduled Message', now, to=['user@gmail.com'])
        email.send()
    except:
        logging.error('E-mail error')