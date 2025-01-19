from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, ConversationHandler, ContextTypes
import logging
import time


async def render_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []
    keyboard.append([InlineKeyboardButton("Расчитать стоимость авто", callback_data="request")])
    keyboard.append([InlineKeyboardButton("Подобрать по параметрам", callback_data="selection")])
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