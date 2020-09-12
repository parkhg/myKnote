import logging
# from config import tgtoken
from telegram.ext import Updater, CommandHandler

# from config import tgtoken
"""
    config file class에 tgtoken 변수를 만드는 것 같음.
"""

# If you send /sum 1 2, your bot will answer The sum is: 3


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

tgtoken = '1128412308:AAH-VncuCy8PUs8u8Sbw84Y0WCoNYXO1x-o'

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def sum(update, context):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1+number2
        update.message.reply_text('The sum is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')

def main():
    updater = Updater(tgtoken, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("sum", sum))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()