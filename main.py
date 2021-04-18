import random
import vk_api
from vk_api.longpoll import groups
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token

vk_session = vk_api.VkApi(token=token)
ts = groups.getL
longpoll_ = VkBotLongPoll(vk_session, 204074660)
vk = vk_session.get_api()
file_read = open('dataBase.txt', 'r', encoding='windows-1251')
temp = file_read.readlines()
file_read.close()

prob = 3

dict_commands = {
    '/пример',
    'глеб',
    'коля'
}


def command_message():
    chat_id = int(event.chat_id)
    random_id = round(random.random() * 10 ** 9)
    if event.text.lower() == '/пример':
        vk.messages.send(  # Отправляем собщение
            chat_id=chat_id,
            random_id=random_id,
            message='Примеррррр'
        )
    if event.text.lower() == 'глеб':
        vk.messages.send(  # Отправляем собщение
            chat_id=chat_id,
            random_id=random_id,
            message='@kok_magic'
        )
    if event.text.lower() == 'коля':
        vk.messages.send(  # Отправляем собщение
            chat_id=chat_id,
            random_id=random_id,
            message='@id235698561'
        )


def usual_message():
    file_write = open('dataBase.txt', 'a', encoding='windows-1251')
    chat_id = int(event.chat_id)
    random_id = round(random.random() * 10 ** 9)
    if event.user_id == 54849868:
        if event.text not in temp:
            temp.append(event.text)
            file_write.write('\n' + temp[-1])
    if random.randint(0, 9) > prob:
        vk.messages.send(  # Отправляем собщение
            chat_id=chat_id,
            random_id=random_id,
            message=temp[random.randint(0, len(temp) - 1)]
        )
    file_write.close()


for event in longpoll_.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        if event.text.lower() in dict_commands:
            command_message()
        else:
            usual_message()

        # print(event.user_id)
        # if event.user_id == 54849868:
        #     if event.from_chat:  # Если написали в Беседе
        #         vk.messages.send(  # Отправляем собщение
        #             chat_id=event.chat_id,
        #             random_id='',
        #             message=' Андрей лох'
        #         )
        #
        # if event.user_id == 205466444:
        #     if random.randint(0, 9) < 3:
        #         if event.from_chat:  # Если написали в Беседе
        #             vk.messages.send(  # Отправляем собщение
        #                 chat_id=event.chat_id,
        #                 random_id='',
        #                 message='Макс крутой'
        #             )

# if __name__ == '__main__':
#     get_history()
