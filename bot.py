token = '1237116120:AAHEbcE0Fi4dQXl2UBkv27l7C6oCgq6SPKs'

import datetime, os # os - to have an opportunity to stop the program's running in an exact form (see code).
def now(): return datetime.datetime.now()

bot = __import__('telebot').TeleBot(token)


@bot.message_handler(commands = ['eval'])
def _eval_(message):
    # with eval(message.text.split(maxsplit = 1)[1]) as res:
        # bot.send_message(699642076, str(res)) # The "str" here should be.
    res = eval(message.text.split(maxsplit = 1)[1])
    bot.send_message(699642076, str(res)) # The "str" here should be (test it or search for more info :) ).

@bot.message_handler(commands = ['kill'])
def SPTR(message):
    print('Reacting...')
    eval('os.kill(os.getppid(), 1234567)')


print(__name__)
bot.send_message(699642076, '.') # Testing purpose.

while True:
    try:bot.polling()
        # u = bot.get_updates
    except Exception as e: print(e); __import__('time').sleep(3)
