# encoding = UTF-8

"""

Simple Bot to reply to Telegram Bot.

"""
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# yellowCatBot Token.
TOKEN = '1128412308:AAH-VncuCy8PUs8u8Sbw84Y0WCoNYXO1x-o'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=TOKEN)
updates = bot.getUpdates()  # Update 내역을 받아온다.

for u in updates:
    print(u.message)

# 가장 최근 메시지ID를 가져옴.
chat_id = updates[-1].message.chat_id
logger.info("chat_id = %s", chat_id)
bot.sendMessage(chat_id=chat_id, text='파스타프ㅏ스타파스타')

logger.info("Telegram Msg Send.")

def run():
    pass
    # bot = telegram.Bot(token=TOKEN)
    # updates = bot.getUpdates()   # Update 내역을 받아온다.
    # # chat_id = updates[-1].message.chat_id
    # # bot.sendMessage(chat_id=chat_id, text='파스타프ㅏ스타파스타')
    #
    # for u in updates:
    #     print(u.message)


    logger.info("Telegram Msg Send.")


if __name__ == '__main__':
    run()
