import telebot
from random import randint
import os



Token = os.environ["TOKEN"]
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start', 'help'])
def greetings(message):
	Text = ("Это бот для определения дежурного. Алгоритм выбора основан на математических алгоритмах,"
	"так что можете не сомневаться в его честности :)\n"
	"Введите /select для случайного выбора дежурного")
	bot.reply_to(message, Text)

@bot.message_handler(commands=['select'])
def choose(message):
	candidates = ['Galym', 'Islam', 'Issa', 'Kostya', 'Aliya', 'Maral', 'Roman', 'Mereke']
	choose = randint(0, len(candidates) - 1)
	text = 'Сегодня дежурным назначается ' + candidates[choose]
	bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def others(message):
	text = "Этот бот очень глуп, и в данный момент не умеют обрабатывать такие команды. Но вы можете поддержать разработчика финансово, а взамен он будет стараться делать бота все лучше."
	bot.reply_to(message, text)



bot.infinity_polling()