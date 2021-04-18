import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import token

prob = 3
vk_session = vk_api.VkApi(token=token)

longpoll_ = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll_.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print(event.user_id)
        if event.user_id == 54849868:
            if event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id='',
                    message=' Андрей лох'
                )
        if event.user_id == 205466444:
            if event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id='',
                    message=' Макс крутой'
                )
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':  # Если написали заданную фразу
            if event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id='',
                    message='bruh'
                )
