from django.core.mail import EmailMessage
from datetime import datetime
from website.models import Candidate
from website.email import scheduledEmail
from django.core.management.base import BaseCommand
import logging

class Command(BaseCommand):
    help = 'Send an e-mail with the number of subscribed candidates today'
    
    def handle(self, *args, **kwargs):
        scheduledEmail()

    def handle2(self, *args, **kwargs):
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