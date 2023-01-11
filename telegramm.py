import requests
import json

def send_msg(text):
    token = "1894081574:AAEURwUheJ5yCuf4eqnL9ecTYeSEEjXevVE"
    chat_id = "1866398473"

    url_req = "https://api.telegram.org/bot" + token +"/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    receve = requests.get(url_req)
    return receve
