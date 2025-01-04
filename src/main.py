import logging

from telegram.ext import ApplicationBuilder, CommandHandler

from bot import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    bot = Bot()
    application = ApplicationBuilder().token(bot.token).build()
    
    # start_handler = CommandHandler('start', command_start)
  
    # application.add_handler(start_handler)
  
    application.run_polling()