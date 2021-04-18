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
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':
            vk.messages.send(  # Отправляем собщение
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Ваш текст'
            )
