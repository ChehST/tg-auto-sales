import logging
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from constants.messages import MENU_RENDER_MESSAGE


async def render_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Расчитать стоимость авто", callback_data="request")])
    # 37-turn-off-selection-command
    # keyboard.append([InlineKeyboardButton("Подобрать по параметрам", callback_data="selection")])
    # also turnoff in main file related callback
    keyboard.append([InlineKeyboardButton("Авто в наличии", callback_data="avaliable")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Issue - if user have restriction to recieve video and audio notes
    # then it will not be sent and next send_message too. Need to catch
    # the exceptions.
    try:
        await context.bot.sendVideoNote(chat_id=update.effective_chat.id,
                                video_note=open('media/video4.mp4', 'rb')
                                )
    except Exception as e:
        logging.error(f"Error sending video note: {e}")

    time.sleep(1)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=MENU_RENDER_MESSAGE,
                                    reply_markup=reply_markup
                                    )
