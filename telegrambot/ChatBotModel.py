import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

class TelegramBot:
    def __init__ (self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token, use_context=True)
        self.name = name

    def sendMessage(self, id, text, reply_markup=None):
        self.core.sendMessage(chat_id = id, text=text, reply_markup=reply_markup)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class WaddleBot(TelegramBot):
    def __init__(self):
        self.token = '1128412308:AAH-VncuCy8PUs8u8Sbw84Y0WCoNYXO1x-o'
        TelegramBot.__init__(self, '와들', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def add_query_handler(self, func):
        self.updater.dispatcher.add_handler(CallbackQueryHandler(func))

    def add_message_handler(self, func):
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, func))

    def add_error_handler(self, func):
        self.updater.dispatcher.add_error_handler(func)

    def start(self):
        print('start')
        self.updater.start_polling()
        self.updater.idle()
