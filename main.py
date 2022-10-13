# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import telebot
import redis

r = redis.StrictRedis()
print(r.ping())

bot = telebot.TeleBot("5312489077:AAFSoXYLLkpjAOh5u4wAZyhmWM19mtE9k3I")

@bot.message_handler()
def start(message):
    user_name = f'Доброе утро, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, user_name, parse_mode="html")

bot.polling(none_stop=True)

