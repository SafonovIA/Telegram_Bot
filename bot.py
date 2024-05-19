import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime


logging.basicConfig(filename="bot.log", level=logging.INFO, encoding="utf-8") # Записи об обшибках в файл bot.log

# Настройки прокси
PROXY = {'proxy_url': settings.bot_key,
         settings.proxy_url: {'username': settings.proxy_username, 'password': settings.proxy_password}}


# Бот
def main():
    mybot = Updater("7049200894:AAFllh6j4GpTIcSRo_OBXxbhoszAc1rsV10",
                    use_context=True)  # Экземпяр бота

    dp = mybot.dispatcher # Диспетчер бота
    dp.add_handler(CommandHandler("start", start)) # обработка команды start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info(f"Бот стартовал {datetime.today()}")
    mybot.start_polling()  # Регулярное обращение к телеге за обновлениями
    mybot.idle()  # Работай постоянно пока не остановили

# Обработка команды /start
def start(update, conterxt):
    print("вызов старт") # Написать в консоль
    update.message.reply_text("Привет") # Ответить пользователю в тг
    print(update.message)

# Обработка текстовых сообщений
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

if __name__ == "__main__":
    main()
