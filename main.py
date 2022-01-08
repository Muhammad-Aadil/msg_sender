import telebot
import json

def get_config():
    with open("config.json", "r") as f:
        return json.loads(f.read())

group_id = -1001776399024
config = get_config()
token = config["token"]

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def welcome_messsage(message):
    bot.send_message(message.chat.id,'Hi, Please provide your Full Name: ')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, "Please provide your email.")
    bot.register_next_step_handler(message, get_email, name)

def get_email(message, name):
    email = message.text.strip()
    bot.send_message(message.chat.id, "Trading News:\nhttps://t.me/+M9hB8-E4JYIyYTFi\n\nTrading Austausch:\n\nhttps://t.me/+VU8qupL_goU3NmI6")
    bot.send_message(group_id, f"Username: {message.from_user.username}\nName: {name}\nEmail: {email}")



print(bot.get_me())
bot.infinity_polling()