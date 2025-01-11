
from telegram import (ReplyKeyboardRemove, ReplyKeyboardMarkup,
                      InlineKeyboardButton, InlineKeyboardMarkup,
                      Update)
from telegram.ext import CommandHandler, MessageHandler, ContextTypes


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
                                   text="Отлично!\n\n" + \
                                        "Выберите вопрос, который интересует и Илья отправит вам персональный ответ.\n\n" + \
                                        "1️⃣ Какие гарантии предоставляете?\n" + \
                                        "2️⃣ Как я могу быть уверен, что меня не обманут?\n" + \
                                        "3️⃣ Какие есть риски при покупке автомобиля из-за рубежа?\n" + \
                                        "4️⃣ Из чего складывается стоимость из из Кореи, Китая и Японии?\n" + \
                                        "5️⃣ Кто осматриваем автомобили, если вы находитесь в России?\n" + \
                                        "6️⃣ Страхуется ли автомобиль во время доставки?\n\n" + \
                                        "Нажмите на цифру 👇",
                                   reply_markup=reply_markup)