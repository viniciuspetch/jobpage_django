from django.core.mail import EmailMessage
from datetime import datetime
from .models import Candidate
import logging

def scheduledEmail():
    today = datetime.today().day
    print("LOG: "+"Today is day {}".format(today))
    query = Candidate.objects.filter(datetime__day=today)
    cdd_qt = len(query)
    email_msg = "There are {} new candidates today.".format(cdd_qt)
    print("LOG: "+email_msg)
    try:
        email = EmailMessage('Scheduled Message', email_msg, to=['user@gmail.com'])
        email.send()
    except:
        print("ERROR: Couldn't send the e-mail")