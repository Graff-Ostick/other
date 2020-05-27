import requests
import random

url = "https://api.telegram.org/bot1123386747:AAEQ8gfTMJ4Bemwz44JLnhyoroqwchzbqbE/"

def last_update(request):
    response = request.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_message_text(update):
    message_text = update['message']['text']
    return message_text

def send_message(chat, text):
    params = {'chat_id' : chat, 'text' : text}
    response = requests.post(url + "sendMessage", data = params)
    return response

def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lover() == 'hi'\
             or get_message_text(update).lover() == "hello" \
             or get_message_text(update).lower() == "hey":
                send_message(get_chat_id(update), 'Greetings! Type game to start')
            elif get_message_text(update).lover() == 'game':
                first_n = random.randint(1, 6)
                second_n = random.randint(1,6)
                send_message(get_chat_id(update), 'You have ' + str(first_n) + ' and ' + str(second_n) + '!\n you result is ' + str(first_n+second_n) \
                + "!")
                update_id += 1
            else:
                send_message(get_chat_id())
