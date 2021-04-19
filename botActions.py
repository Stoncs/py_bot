import requests
import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token


def command_message(text, user_id, chat_id, vk):
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


def usual_message(text, user_id, chat_id, vk, temp):
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