from telebot import TeleBot
from commands.low import low_controller
from keyboards import main_markup

TOKEN = "6169901067:AAECICykWk9DQ3mmhHvdR5mU_FZXMtIEaPE"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['low'])
def low(message):
    low_controller(message, bot)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Выберите действие',reply_markup=main_markup())



bot.polling()