import random

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token

vk_session = vk_api.VkApi(token=token)
# Получаем данные сессии
vk = vk_session.get_api()
longpoll_ = VkBotLongPoll(vk_session, 204074660)
file_read = open('dataBase.txt', 'r', encoding='windows-1251')
temp = file_read.readlines()
file_read.close()
data = requests.get('https://api.vk.com/method/messages.getLongPollServer', params={'access_token': token, 'v': 5.21}).json()['response']

prob = 3

dict_commands = {
    '/пример',
    'глеб',
    'коля'
}


def command_message(text, user_id, chat_id):
    random_id = round(random.random() * 10 ** 9)
    if text.lower() == '/пример':
        vk.messages.send(  # Отправляем собщение
            access_token=token,
            chat_id=chat_id,
            random_id=random_id,
            message='Примеррррр'
        )
    if text.lower() == 'глеб':
        vk.messages.send(  # Отправляем собщение
            access_token=token,
            chat_id=chat_id,
            random_id=random_id,
            message='@kok_magic'
        )
    if text.lower() == 'коля':
        vk.messages.send(  # Отправляем собщение
            access_token=token,
            chat_id=chat_id,
            random_id=random_id,
            message='@id235698561'
        )


def usual_message(text, user_id, chat_id):
    file_write = open('dataBase.txt', 'a', encoding='windows-1251')
    random_id = round(random.random() * 10 ** 9)
    if user_id == '54849868':
        if not temp.__contains__(text):
            temp.append(text)
            file_write.write('\n' + temp[-1])
    if random.randint(0, 9) < 10 and user_id != '-204074660':
        vk.messages.send(  # Отправляем собщение
            access_token=token,
            chat_id=chat_id,
            random_id=random_id,
            message=temp[random.randint(0, len(temp) - 1)]
        )
    file_write.close()


# for event in longpoll_.listen():
#     if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
#         if event.text.lower() in dict_commands:
#             command_message()
#         else:
#             usual_message()


while True:
    response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()
    updates = response['updates']
    if updates:  # проверка, были ли обновления
        for element in updates:  # проход по всем обновлениям в ответе
            action_code = element[0]
            if action_code == 4:
                text = element[5]
                user_id = element[6]['from']
                chat_id = element[3] - 2000000000
                print(text)
                if text in dict_commands:
                    command_message(text, user_id, chat_id)
                else:
                    usual_message(text, user_id, chat_id)

    data['ts'] = response['ts']  # обновление номера последнего обновления


# # Получаем лонгпул

