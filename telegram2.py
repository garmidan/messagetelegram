# importar todas las bibliotecas requeridas
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel, InputChannelEmpty
from telethon import TelegramClient, sync, events 
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types.messages import Messages
from telethon.tl.types.contacts import Contacts
from telethon.tl.functions.contacts import GetContactsRequest 
# obtener datos de la api (api_id, api_hash, token)
# desde el telegrama como se describe arriba
api_id = '2874192'
api_hash = 'e0010897cd27a19d8722b1d9450400f9'
token = 'bot1444469431:AAHGiijQJ952yuD8MA2TBLQKQs4uovypng4'
# Numero de celular 
phone = '+573186492691'
   
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
    contacts = client(GetContactsRequest(0))
    # recorrer todos los numeros de telefono
    for u in contacts.users: 
        # validar que sea el numero de telefono al que le quiero enviar el mensaje
        if u.phone == "573123189219":
            client.send_message(InputPeerUser(u.id, u.access_hash), "Hola desde python") 
            # enviando mensaje usando el cliente de telegram 
            print("Mensaje Enviado a cliente telegram")
except Exception as e: 
      
    # there may be many error coming in while like peer 
    # confirmar el error
    print(e)
  
# desconectando la sesión de telegrama  
client.disconnect() 