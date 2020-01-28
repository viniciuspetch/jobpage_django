import website.telegrambot as bot
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Bot command'
    
    def handle(self, *args, **kwargs):
        bot.begin()