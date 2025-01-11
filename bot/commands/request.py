
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler, ContextTypes
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