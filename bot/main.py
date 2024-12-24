import os
import logging
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler
)
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
                                video_note=open('media/video3.mp4', 'rb'),
                                reply_markup=reply_markup)

async def command_request(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("Готов к покупке", callback_data="request_hot_lead")],
        [InlineKeyboardButton("Присматриваюсь", callback_data="request_warm_lead")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Сейчас наша компания ощущает огромный спрос на автомобили.\n\n" + \
                                        "✅ Готовы к покупке в течение 30 дней? Направим вас сразу\
                                        к эксперту по импорту, чтобы ускорить процесс.\n\n" + \
                                        "👀 Ещё присматриваетесь? Мы подготовим предложение в \
                                              течение 2-3 дней, чтобы вы могли всё обдумать.\n\n" + \
                                        "❗️Пожалуйста, выбирайте внимательно. Это поможет снизить нагрузку, направить\
                                            запрос в нужный отдел и обеспечить вам быстрый расчёт и лучшее обслуживание.\n\n" + \
                                        "🗨️ Вы готовы к покупке или присматриваетесь?\n\n" + \
                                        "Жмите на кнопку ниже 👇",
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
    await context.bot.sendVideoNote(chat_id=update.effective_chat.id,
                                video_note=open('media/video4.mp4', 'rb')
                                )

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

async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data['lead_category'] = query.data
    # Set user awaiting instance
    context.user_data['state'] = 'awaiting_car_model'
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="[1/3] Какие марки и модели авто вас интересуют?\n\n" + \
                "Напишите ниже в произвольной форме 👇"
        )



async def text_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = context.user_data.get('state')

    button = [[KeyboardButton("✅Получить расчёт",request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(button,resize_keyboard=True)

    if state == 'awaiting_car_model':
        car_model = update.message.text
        context.user_data['car_model'] = car_model
        context.user_data['state'] = 'awaiting_car_budget'  # Переход к следующему состоянию

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="[2/3] На какой бюджет вы рассчитываете?\n\n" + \
                "Пожалуйста, напишите ниже в числовом формате, в рублях.\n\n" + \
                "⚠️ Не пишите слова или знаки валют, только числа.\n" + \
                "(примеры: 2000000, 3500000, 4300000)"
        )

    elif state == 'awaiting_car_budget':
        # Обработка следующего этапа

        car_budget = update.message.text
        context.user_data['car_budget'] = car_budget
        context.user_data['state'] = 'awaiting_phone_number'  # Завершение последовательности
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="😊 Остался последний шаг!\n\n" + \
                    'Нажмите кнопку "Получить расчёт",' + \
                    ' и мы отправим вам стоимость в мессенджеры или перезвоним.\n\n' + \
                    "Хотите написать сами?\n"
                    "👉 Связаться с экспертом:",
                    reply_markup=reply_markup
        )

async def contact_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('state') == 'awaiting_phone_number':
        contact = update.message.contact
        if contact:
            phone_number = contact.phone_number
            context.user_data['phone'] = phone_number

            # Send final message with all collected information
            car_model = context.user_data.get('car_model')
            car_budget = context.user_data.get('car_budget')
            lead_category = context.user_data.get('lead_category')


            # Debug output, it might be good to create ticket to add
            # flag DEBUG_MODE to print this info into log file instead of console
            # or just remove it after testing phase
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Клиент категории {lead_category}.Вы заказали расчет стоимости авто {car_model} на бюджет {car_budget}. Ваш номер телефона: {phone_number}"
            )

            context.user_data['state'] = None

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
        await command_request(update, context)
    if query.data == 'selection':
        pass
    if query.data == 'avaliable':
        await command_avaliable(update, context)
    if query.data == 'link_to_your_channel':
        pass
    if query.data in ['request_hot_lead', 'request_warm_lead']:
        await handle_order(update, context)
    

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN_BOT')).build()
    
    start_handler = CommandHandler('start', command_start)
    avaliable_handler = CommandHandler('avaliable', command_avaliable)
    request_handler = CommandHandler('request', command_request)
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, text_input_handler)
    contact_handler = MessageHandler(filters.CONTACT, contact_input_handler)
    application.add_handler(contact_handler)
    application.add_handler(text_handler)
    application.add_handler(start_handler)
    application.add_handler(avaliable_handler)
    application.add_handler(request_handler)
    application.add_handler(CallbackQueryHandler(button_callback))
    application.run_polling()