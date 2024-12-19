import os
import logging
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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

    await context.bot.sendVideoNote(chat_id=update.effective_chat.id,
                                video_note=open('media/video1.mp4', 'rb'),
                                reply_markup=reply_markup)

async def command_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = [[KeyboardButton("Получить расчёт",request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(button)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Типа диалог 1/2")
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Типа диалог 2/2")
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Заявка заполнена, нажмите кнопку ниже 👇",
                                   reply_markup=reply_markup)

async def command_avaliable(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Авто в наличии", callback_data="link_to_your_channel")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open('media/image2.jpg', 'rb'),
                                 caption="Наш Telegram-канал с автомобилями, уже \
                                      проверенными и готовыми к покупке!\n\n" + \

                                    "❗️Все авто в наличии, доставка в РФ - до 30 дней.\n"+\
                                    "🔥 Экономьте до 2 000 000 ₽ от рыночной стоимости!\n\n" + \

                                    "Ссылка на канал:\n" + \
                                    "👉 https://linktoyourchanel\n\n" + \

                                    "Что вас ждёт:\n" +\
                                    "▪️ Новые авто из Китая по ценам производителя\n" + \
                                    "▪️ Поддержанные авто из Китая и Кореи с полным осмотром\n\n" + \


                                    "За их состояние и точность описания мы отвечаем лично!\n\n" + \

                                    "Подписывайтесь, чтобы первыми видеть лучшие предложения!\n\n" + \

                                    '👉 Нажмите на кнопку "Авто в наличии"',
                                 reply_markup=reply_markup
    )

async def render_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Расчитать стоимость авто", callback_data="request")])
    keyboard.append([InlineKeyboardButton("Подобрать по параметрам", callback_data="selection")])
    keyboard.append([InlineKeyboardButton("Авто в наличии", callback_data="avaliable")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Issue - if user have restriction to recieve video and audio notes
    # then it will not be sent and next send_message too. Need to catch
    # the exceptions.
    # await context.bot.sendVideoNote(chat_id=update.effective_chat.id,
    #                             video_note=open('media/video2.mp4', 'rb')
    #                             )

    time.sleep(1)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text="Что вас интересует дальше?\n\n" + \

                                        "💰Расчёт стоимости авто:\n" + \
                                        "Рассчитаем стоимость авто с доставкой и таможней под ключ" + \
                                        "- для тех, кто уже присматривается или готов к покупке.\n\n" + \

                                        "📝 Подбор авто по параметрам:\n" + \
                                        "Получите подборку автомобилей по вашим критериям.\n\n" +\

                                        "🚗 Авто в наличии: Проверенные автомобили, \
                                          которые уже есть в наличии, доставка в РФ - до 30 дней.\n\n" + \

                                        "Жмите кнопку ниже 👇",
                                    reply_markup=reply_markup
                                    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles callback queries from inline keyboard buttons.

    Args:
        update (Update): Incoming update.
        context (ContextTypes.DEFAULT_TYPE): Context for the callback.

    This function checks the data of the callback query and sends a message
    with an invite link if the data matches 'invite_link'.
    """
    
    query = update.callback_query
    await query.answer()
    if query.data == 'menu':
        await render_menu(update, context)
    if query.data == 'request':
        pass
    if query.data == 'selection':
        pass
    if query.data == 'avaliable':
        await command_avaliable(update, context)
    if query.data == 'link_to_your_channel':
        pass
    

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN_BOT')).build()
    
    start_handler = CommandHandler('start', command_start)
    avaliable_handler = CommandHandler('avaliable', command_avaliable)
    request_handler = CommandHandler('request', command_request)
    application.add_handler(start_handler)
    application.add_handler(avaliable_handler)
    application.add_handler(request_handler)
    application.add_handler(CallbackQueryHandler(button_callback))
    application.run_polling()
