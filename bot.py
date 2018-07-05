import telebot
import hashlib

TOKEN = "577347064:AAGatkwrANH7KL2psoRLEbplfxpo21gE3WE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, я HashBot, могу сделать хэши md5 и sha1 из любой строки, которую ты мне пришлёшь!\nПросто напиши)')
@bot.message_handler(commands = ['md5'])
def md5_hashing(message):
    sent = bot.send_message(message.chat.id, 'Пришли строку)')
    bot.register_next_step_handler(sent,md5_hashed)
def md5_hashed(message):
    bot.send_message(message.chat.id, 'Готово: ' + hashlib.md5(message.text.encode()).hexdigest())
@bot.message_handler(commands = ['sha1'])
def sha1_hashing(message):
    sent = bot.send_message(message.chat.id, 'Пришли строку)')
    bot.register_next_step_handler(sent,sha1_hashed)
def sha1_hashed(message):
    bot.send_message(message.chat.id, 'Готово: ' + hashlib.sha1(message.text.encode()).hexdigest())

bot.polling()