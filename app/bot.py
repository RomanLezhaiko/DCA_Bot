import os
from random import randint
import matplotlib.pyplot as plt

from telebot import TeleBot, types
from dotenv import load_dotenv

from settings_file import SettingsFile

settings = SettingsFile()


load_dotenv()
TOKEN = os.getenv("TG_TOKEN")
bot = TeleBot(TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonCommands('commands'))
    bot.send_message(message.chat.id, f'Hi there, {message.chat.id}')


@bot.message_handler(commands=['get_data'])
def start_handler(message):
    # x = [0, 1, 2, 3, 4, 5]
    # y = [100, 200, 150, 210, 230, 300]
    # y_1 = [100, 120, 130, 150, 170, 200]
    
    x = [i for i in range(1000)]
    y = [randint(170, 300) for _ in range(1000)]
    y_1 = [randint(100, 150) for _ in range(1000)]
    

    plt.plot(x, y, label='Текущая цена')
    plt.plot(x, y_1, label='Средняя цена')
    plt.title('Line Graph')
    plt.xlabel('Даты')
    plt.ylabel('Цена')
    plt.legend()
    file_path = os.path.join(os.getcwd(), 'test.png')
    plt.savefig(file_path, bbox_inches='tight')
    # bot.send_message(message.chat.id, f'Hi there, {message.chat.id}')
    with open(file_path, 'rb') as file:
        bot.send_photo(message.chat.id, file, caption='Test caption')
    
    os.remove(file_path)


@bot.message_handler(commands=['set_token'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Enter the token')
    bot.register_next_step_handler(message, test)


def test(message):
    bot.send_message(message.chat.id, f'Your token is: {message.text}')
    user = message.from_user.username
    bot.send_message(message.chat.id, f'@{user}')


bot.set_my_commands(
    commands=[
        types.BotCommand('start', 'Start bot'),
        types.BotCommand('get_data', 'Get data'),
        types.BotCommand('set_token', 'Set token'),
    ]
)

bot.infinity_polling()