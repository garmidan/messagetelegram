import requests

def telegram_bot_sendtext(bot_message):
   bot_token = '1444469431:AAHGiijQJ952yuD8MA2TBLQKQs4uovypng4'
   bot_chatID = '-411732112'
   bot_message = 'Mensaje enviado desde python 3'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)