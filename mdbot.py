import telebot
import extention



		
capi= extention.APIWorker
#print(capi.get_price('USD','BTC',1))
#print(capi.getCoinList())

	
token='6010668394:AAESVMGTK8ZAtCkq6WckoAbQJOI0SCzpRZo'

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['help', 'start'])
def func_start(message):
	bot.send_message(message.chat.id, '💥 Бот стоимости валюты 💥\n'
    '🔹/start - запустить бота \n'+
    '🔹/help - получить справку по командам\n'+
    '🔹/values - получить список цифровых валют\n\n'+
    '💰 для перевода из одной валюты в другую, необходимо указать валюты в следующей последователтности:\n'+ '<исходная валюта> <валюта конвертации> <количество исходной валюты>\n'+
    'Первые два аргумента должны соотвествать существующим валютам из списка /values, последний аргумент должен быть всегда положителтным числом\n\n'
    'Примеры:\n'+
    '🔹USD BTC 8 - в результате 8 USD будет переведено а BTC\n'+
    '🔹BTC USD 4 - в результате 4 BTC будет переведено а USD')

@bot.message_handler(commands=['values'])
def func_coins(message):
        bot.send_message(message.chat.id, capi.getValuesList())

@bot.message_handler()
def usercommand(message):
    result=message.text.split(' ')
    if(len(result)==3):
    	if(result[0].isnumeric()==False and result[1].isnumeric()==False and result[2].isnumeric()==True):
    		bot.send_message(message.chat.id, capi.get_price(result[0].upper(),result[1].upper(),int(result[2])))
    	else:
    		bot.send_message(message.chat.id,'Ошибка ввода: один из аргументов введен неверно, содержит несуществующие названия валют или цифры с символами. Для справки наберите команду /help')
    else:
    	bot.send_message(message.chat.id,'Ошибка ввода: необходимо ввести три аргумента, для справки наберите команду /help')
    	
bot.polling()


print("MDCurrencyBot")