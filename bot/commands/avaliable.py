
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update
from telegram.ext import CallbackContext, CommandHandler,ContextTypes


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