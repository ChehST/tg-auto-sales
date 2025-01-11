import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
import time

async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Продолжить", callback_data="menu")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open('media/team.png', 'rb'),
                                 caption="👋 Привет, " + update.effective_chat.first_name + "!" + \
                                         "Это бот компании АвтоНаходка.\n\n"

                                         "🚗 Мы помогаем приобрести новые и поддержанные автомобили из Китая, \
                                            Кореи и Японии, сэкономить до 2 000 000 ₽ и получить их за 15-45 дней!\n\n" + \

                                         "Далее расскажем, почему авто из Азии в лучшем состоянии, \
                                            а их покупка - выгодна и безопасна.\n\n"

                                         "⚠️ Чтобы получить максимальную пользу от бота, \
                                            выбирайте подходящие варианты ответов, нажимая на соответствующие кнопки.\n\n" + \

                                         "Важно❗\n" + \
                                         "Выбор можно сделать только один раз.\
                                            Пожалуйста выбирайте внимательно, так как после нажатия кнопки \
                                            изменить его не получится.\n\n" + \

                                         "❌ Обратите внимание: здесь не ведутся диалоги. \
                                            Чтобы определить, как мы можем помочь и к какому \
                                            специалисту вас направить, ответьте на вопросы бота.\n\n" + \

                                         "Жмите на кнопку ниже 👇",
                                 reply_markup=reply_markup )

    time.sleep(3)

    try:
        await context.bot.sendVideoNote(chat_id=update.effective_chat.id,
                                video_note=open('media/video3.mp4', 'rb'),
                                reply_markup=reply_markup)
    except Exception as e:
        logging.error(f"Error sending video note: {e}")
