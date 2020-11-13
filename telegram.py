import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
  
   
# obtener datos tu api_id, api_hash, token
# desde el telegrama como se describe arriba
api_id = '2874192'
api_hash = 'e0010897cd27a19d8722b1d9450400f9'
token = '1423511548:AAHbPNz1VyC61NZVaN6M1ubdVhqrKpjBGQ4'
  
import requests

def telegram_bot_sendtext(bot_message):
   bot_token = '1444469431:AAHGiijQJ952yuD8MA2TBLQKQs4uovypng4'
   bot_chatID = '-411732112'
   bot_message = 'Mensaje enviado desde python 2'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)