import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

vk_session = vk_api.VkApi(token=token)

longpoll_ = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll_.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    random_id=event.user_id,
                    message='Ваш текст'
		)