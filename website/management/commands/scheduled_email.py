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