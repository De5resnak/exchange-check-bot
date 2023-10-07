from config import token, list_of_values
import telebot
import extensions as ex


bot = telebot.TeleBot(token = token)
@bot.message_handler(commands=["help","start"])
def start_ans(message):
    bot.reply_to(message, """Привет! Для начала работы бота отправь сообщение в виде:\n<имя валюты> 
<имя валюты> <количество первой валюты>\nПример:\nДоллар Рубль 54\n
Если вы хотите узнать доступные для перевода валюты, введите команду\n/values""")

@bot.message_handler(commands=["values"])
def values_ans(message):
    ans = "Доступные для перевода валюты:\n"
    for i in list_of_values:
        ans+= i+"\n"
    bot.reply_to(message,text=ans)
@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        message.text = message.text.lower()
        while "  " in message.text:
            message.text = message.text.replace("  ", " ")
        values = message.text.split(' ')
        if len(values) != 3:
            raise ex.ConvertException("вы указали неверное количество аргументов")
        base = values[0]
        quote = values[1]
        amount = values[2]
        text = "Цена "+values[2] +" " + values[0] +" в " + values[1] + " равна " + str(ex.Converse.get_price(base,quote,amount))
    except ex.APIError as e:
        bot.reply_to(message, e)
    except ex.ConvertException as e:
        bot.reply_to(message, e)
    except Exception as e:
        bot.reply_to(message, e)
    else:
        bot.reply_to(message, text)

bot.polling(none_stop = True)
