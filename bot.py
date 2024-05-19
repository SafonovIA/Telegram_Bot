import logging
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime


logging.basicConfig(filename="bot.log", level=logging.INFO, encoding="utf-8") # Записи об обшибках в файл bot.log

# Настройки прокси
PROXY = {'proxy_url': settings.bot_key,
         settings.proxy_url: {'username': settings.proxy_username, 'password': settings.proxy_password}}


# Бот
def main():
    mybot = Updater("7049200894:AAFllh6j4GpTIcSRo_OBXxbhoszAc1rsV10",
                    use_context=True)  # Экземпяр бота

    dp = mybot.dispatcher # Диспетчер бота
    dp.add_handler(CommandHandler("start", start))  # обработка команды start
    dp.add_handler(CommandHandler("planet", planet_comand))  # обработка команды start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # Обработка входящего текста

    logging.info(f"Бот стартовал {datetime.today()}")  # Запись в логи что бот стартовал
    mybot.start_polling()  # Регулярное обращение к телеге за обновлениями
    mybot.idle()  # Работай постоянно пока не остановили

# Обработка команды /start
def start(update, conterxt):
    print("вызов старт") # Написать в консоль
    update.message.reply_text("Привет") # Ответить пользователю в тг


# Обработка текстовых сообщений
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

# Обработка команды "/planet" (возвращает созведие планеты)
def planet_comand(update, conterxt):
    planet = update.message.text.split()[1]
    if planet == "Mars":
        pl = ephem.Mars(date.today())
    elif planet == "Mercury":
        pl = ephem.Mercury(date.today())
    elif planet == "Venus":
        pl = ephem.Venus(date.today())
    elif planet == "Earth":
        pl = ephem.Earth(date.today())
    elif planet == "Jupiter":
        pl = ephem.Jupiter(date.today())
    elif planet == "Saturn":
        pl = ephem.Saturn(date.today())
    elif planet == "Uranus":
        pl = ephem.Uranus(date.today())
    elif planet == "Neptune ":
        pl = ephem.Neptune(date.today())
    elif planet == "Pluto ":
        pl = ephem.Pluto(date.today())
    elif planet == "Sun":
        pl = ephem.Sun(date.today())
    elif planet == "Moon":
        pl = ephem.Moon(date.today())
    else:
        update.message.reply_text("No planet found")
    update.message.reply_text(f"'{pl.name}' in the constellation {ephem.constellation(pl)[1]}")


if __name__ == "__main__":
    main()
