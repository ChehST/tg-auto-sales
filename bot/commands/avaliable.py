from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update
from telegram.ext import ContextTypes

from constants.messages import AVAILABLE_MESSAGE


async def command_avaliable(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Авто в наличии", callback_data="link_to_your_channel")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open('media/image2.jpg', 'rb'),
                                 caption=AVAILABLE_MESSAGE,
                                 reply_markup=reply_markup
    )
