# importar todas las bibliotecas requeridas
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
  
   
# obtener datos de la api (api_id, api_hash, token)
# desde el telegrama como se describe arriba
api_id = 'API_id'
api_hash = 'API_hash'
token = 'bot token'
  
# Numero de celular 
phone = 'YOUR_PHONE_NUMBER_WTH_COUNTRY_CODE'
   
# creando una sesión de telegrama y asignando
# Variable cliente 
client = TelegramClient('session', api_id, api_hash) 
   
# Probar conexion de telegram
client.connect() 
  
# en caso de que el script se ejecute por primera vez
# pida que introduzca el token o el otp enviado a
# número enviado o su ID de telegrama
if not client.is_user_authorized(): 
   
    client.send_code_request(phone) 
      
    # firmando en el cliente
    client.sign_in(phone, input('Enter the code: ')) 
   
   
try: 
    # El receptor
    receiver = InputPeerUser('user_id', 'user_hash') 
  
    # enviando mensaje usando el cliente de telegram 
    client.send_message(receiver, "Message", parse_mode='html') 
except Exception as e: 
      
    # there may be many error coming in while like peer 
    # confirmar el error
    print(e)
  
# desconectando la sesión de telegrama  
client.disconnect() 