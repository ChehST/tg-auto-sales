import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  ContextTypes


from config import ADMIN
logger = logging.getLogger(__name__)


async def settings_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
     # Создание кнопки для установки менеджера
    button = [[InlineKeyboardButton("Установить менеджера", callback_data='set_manager')]]
    reply_markup = InlineKeyboardMarkup(button)
    try:
        user_id = update.effective_user.id
        if user_id != ADMIN:
            raise PermissionError(f"У вас нет доступа к этой команде. Admin:{ADMIN}")
        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Выберите действие:",
            reply_markup=reply_markup
        )
    except PermissionError as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(e)
            
        )
        logger.error(f"Error: {e}")
