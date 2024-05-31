import telebot
import open_weather_data

API_TOKEN = 'Токен можно получить в ТГ у https://t.me/BotFather'
bot = telebot.TeleBot(API_TOKEN)

# Example 1 Отправка сообщения
# message_handler - функция обрабатывает все сообщения пользователя
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)


# Example 2 Ответ на сообщение
# @bot.message_handler(func=lambda message: True)
# def echo_reply(message):
#     bot.reply_to(message, message.text)


# Example 3 Добавление клавиатуры
# @bot.message_handler(func=lambda message: True)
# def echo_this_keyboard(message):
#     keyboard_last_word = telebot.types.ReplyKeyboardMarkup(True)
#     keyboard_last_word.row(message.text)
#     bot.send_message(message.chat.id, message.text, reply_markup=keyboard_last_word)


# Example 4 Бот погоды
# message_handler - функция реагирует только на команды
# @bot.message_handler(commands=['help', 'start'])
# def welcome_msg(message):
#     bot.send_message(message.chat.id, 'Напишите город, в котором хотите узнать погоду')
#
#
# @bot.message_handler(func=lambda message: True)
# def view_weather(message):
#     city_weather_keyboard = telebot.types.ReplyKeyboardMarkup(True)
#     weather_data = open_weather_data.get_open_weather_one_day(message.text)
#     if not weather_data.startswith('Напишите'):
#         city_weather_keyboard.row(message.text)
#     bot.send_message(message.chat.id, weather_data, reply_markup=city_weather_keyboard)


bot.polling(non_stop=True, interval=0)
