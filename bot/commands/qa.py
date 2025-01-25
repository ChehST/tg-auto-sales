from telegram import (InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      Update)
from telegram.ext import  ContextTypes

from constants.messages import QA_MESSAGE


async def command_qa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    keyboard.append([InlineKeyboardButton("1️⃣", callback_data="faq_1"),
                     InlineKeyboardButton("2️⃣", callback_data="faq_2"),
                     InlineKeyboardButton("3️⃣", callback_data="faq_3")])
    keyboard.append([InlineKeyboardButton("4️⃣", callback_data="faq_4"),
                     InlineKeyboardButton("5️⃣", callback_data="faq_5"),
                     InlineKeyboardButton("6️⃣", callback_data="faq_6")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=QA_MESSAGE,
                                   reply_markup=reply_markup)
