import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
import time

from constants.messages import START_GREETING_MESSAGE

async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Продолжить", callback_data="menu")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    first_name = update.effective_chat.first_name

    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open('media/team.png', 'rb'),
                                 caption=START_GREETING_MESSAGE.format(first_name=first_name),
                                 reply_markup=reply_markup )

    time.sleep(3)

    try:
        await context.bot.sendVideoNote(chat_id=update.effective_chat.id,
                                video_note=open('media/video3.mp4', 'rb'),
                                reply_markup=reply_markup)
    except Exception as e:
        logging.error(f"Error sending video note: {e}")
