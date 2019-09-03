from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from website.models import Candidate
import logging

token = "934290516:AAGXaUOZDW-33pnwNyZUAHXmbwacnCVzSR8"
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def botVagasRits(update, context):
    update.message.reply_text("I'll send those candidates soon")
    list = Candidate.objects.all()
    latest = Candidate.objects.order_by('-datetime')[:3]
    update.message.reply_text("There are {} candidates.".format(len(list)))
    update.message.reply_text("The latest 3 are: {}, {}, {}".format(
        latest[0].email, latest[1].email, latest[2].email))

def botEcho(update, context):
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def begin():
    updater = Updater(token, use_context=True)
    dp= updater.dispatcher
    dp.add_handler(CommandHandler("VagasRits", botVagasRits))
    dp.add_handler(MessageHandler(Filters.text, botEcho))

    
    # log all errors
    dp.add_error_handler(error)


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    begin()