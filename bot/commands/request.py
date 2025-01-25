from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler, ContextTypes

from constants.messages import REQUEST_MESSAGE


async def command_request(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("Готов к покупке", callback_data="HotLead")],
        [InlineKeyboardButton("Присматриваюсь", callback_data="WarmLead")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=REQUEST_MESSAGE,
                                   reply_markup=reply_markup)
