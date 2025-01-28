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
load_dotenv()
import csv


from commands import *
from config import ADMIN


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
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
    reply_markup = ReplyKeyboardMarkup(button)

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
    
    if state == 'awaiting_manager_id':
        try:
            manager_id = int(update.message.text)
            context.bot_data['manager_id'] = manager_id
            context.user_data['state'] = None  # Сбрасываем состояние
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"ID менеджера успешно установлен: {manager_id}"
            )
        except ValueError:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Ошибка: Пожалуйста, введите корректное целое число."
            )

async def contact_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('state') == 'awaiting_phone_number':
        contact = update.message.contact
        if contact:
            phone_number : str | None  = contact.phone_number
            context.user_data['phone'] = phone_number

            # Send final message with all collected information
            username : str = update.effective_user.username
            user_name : str = update.effective_user.first_name
            car_model : str = context.user_data.get('car_model')
            car_budget : int = context.user_data.get('car_budget')
            lead_category : str = context.user_data.get('lead_category')
            user_comment : str | None


            # Получаем ID менеджера или используем ID главного администратора
            manager_id = context.bot_data.get('manager_id', ADMIN)

            # Отправляем заявку менеджеру или главному администратору
            await context.bot.send_message(
                chat_id=manager_id,
                text=f"Новая заявка от клиента категории {lead_category}.\n" +
                     f"Модель авто: {car_model}\n" +
                     f"Бюджет: {car_budget}\n" +
                     f"Телефон: {phone_number}"
            )

            # Если менеджер не установлен, уведомляем главного администратора
            if manager_id == ADMIN:
                await context.bot.send_message(
                    chat_id=ADMIN,
                    text="Менеджер не установлен. Пожалуйста, настройте менеджера через команду /settingsBot."
                )

            # Save data to CSV file that will be used later
            # by sellers
            with open('/var/autoBot/contacts.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # create timestamp field in format dd/mm/yyyy hh:mm
                creation_time = time.strftime("%d/%m/%Y %H:%M")
                user_comment = None
                writer.writerow(
                    [
                        creation_time,
                        username,
                        phone_number,
                        user_name,
                        car_model,
                        car_budget,
                        lead_category,
                        user_comment,
                    ]
                )

            # Debug output, it might be good to create ticket to add
            # flag DEBUG_MODE to print this info into log file instead of console
            # or just remove it after testing phase
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Ваша заявка была успешно отправлена менеджеру. Ожидайте ответа."
            )

            context.user_data['state'] = None
        # here impliment if phone number would not be provided #34

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles callback queries from inline keyboard buttons.

    Args:
        update (Update): Incoming update.
        context (ContextTypes.DEFAULT_TYPE): Context for the callback.

    This function checks the data of the callback query and sends a message
    with an invite link if the data matches 'invite_link'.
    """
    
    plate_keyboard = []
    plate_keyboard.append([InlineKeyboardButton("Остались вопросы?", callback_data="qa")])
    plate_keyboard.append([InlineKeyboardButton("Расчитать стоимость авто", callback_data="request")])
    reply_plate_markup = InlineKeyboardMarkup(plate_keyboard)

    query = update.callback_query
    await query.answer()
    if query.data == 'menu':
        await render_menu(update, context)
    if query.data == 'request':
        await command_request(update, context)
    if query.data == "qa":
        await command_qa(update, context)
    if query.data == 'selection':
        pass
    if query.data == 'avaliable':
        await command_avaliable(update, context)
    if query.data == 'link_to_your_channel':
        pass
    if query.data == 'set_manager':
        # Установка ID менеджера в состояние
        context.bot_data['manager_id'] = query.from_user.id
        context.user_data['state'] = 'awaiting_manager_id'
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="Пожалуйста, введите ID менеджера (целое число):\n\n"+\
                 "Для этого менеджер должен узнать свой ID и сообщить его вам\n\n"+\
                 "Узнать ID можно тут @getidsbot"
        )
    if query.data in ['HotLead', 'WarmLead']:
        await handle_order(update, context)
    if query.data == "faq_1":
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="Мы предоставляем гарантию на все наши услуги и сделки.\n\n" + \
                                            "Если вы столкнетесь с проблемой, связанным с покупкой автомобиля,\
                                                мы будем рады помочь вам решить ее.",
                                       reply_markup=reply_plate_markup)
    if query.data == "faq_2":
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="Мы используем различные методики проверки и осмотра автомобилей,\n\n" + \
                                            "чтобы гарантировать, что они соответствуют высоким стандартам качества.",
                                       reply_markup=reply_plate_markup)
    if query.data == "faq_3":
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="Мы понимаем, что покупка автомобиля из-за рубежа может быть рискована.\n\n" + \
                                            "Поэтому мы предлагаем различные гарантии и страховки, чтобы защитить ваши интересы.",
                                       reply_markup=reply_plate_markup)
    if query.data == "faq_4":
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="Мы берём во внимание все факторы, влияющие на стоимость автомобиля,\n\n" + \
                                            "включая его марку, модель, год выпуска и другие характеристики.",
                                       reply_markup=reply_plate_markup)
    if query.data == "faq_5":
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="Мы работаем с экспертами по импорту автомобилей,\n\n" + \
                                            "которые имеют опыт работы с авто из разных стран.",
                                       reply_markup=reply_plate_markup)
    if query.data == "faq_6":
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="Мы страхуем автомобили во время доставки,\n\n" + \
                                            "чтобы защитить ваши интересы в случае любого несчастного случая.",
                                       reply_markup=reply_plate_markup)
    

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN_BOT')).build()
    
    start_handler = CommandHandler('start', command_start)
    avaliable_handler = CommandHandler('avaliable', command_avaliable)
    request_handler = CommandHandler('request', command_request)
    qa_handler = CommandHandler('qa', command_qa)
    settings_bot_handler = CommandHandler('settingsBot', settings_bot)
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, text_input_handler)
    contact_handler = MessageHandler(filters.CONTACT, contact_input_handler)
    application.add_handler(contact_handler)
    application.add_handler(text_handler)
    application.add_handler(settings_bot_handler)
    application.add_handler(start_handler)
    application.add_handler(qa_handler)
    application.add_handler(avaliable_handler)
    application.add_handler(request_handler)
    application.add_handler(CallbackQueryHandler(button_callback))
    application.run_polling()