import random

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import token
from botActions import command_message, usual_message

vk_session = vk_api.VkApi(token=token)
# Получаем данные сессии
vk = vk_session.get_api()
# chats = vk.messages.getConversationsById(peer_ids=[204074660])
# while True:
#     try:
#         $this->sendMessage(2000000000 + $i, $message);
#         $count++
#     except:
#         if $e->getCode() == 10:
#             //значит такой беседы уже не существует, т.к. она является последней
#             exit($count)
#


# print(chats)
# for chat in chats['items']:
#     print(chat)
longpoll_ = VkBotLongPoll(vk_session, 204074660)
file_read = open('dataBase.txt', 'r', encoding='windows-1251')
temp = file_read.readlines()
file_read.close()
data = requests.get('https://api.vk.com/method/groups.getLongPollServer', params={'access_token': token, 'v': 5.21,
                                                                                  'group_id':204074660}).json()['response']

prob = 3

dict_commands = {
    '/пример',
    'глеб',
    'коля'
}








# for event in longpoll_.listen():
#     if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
#         if event.text.lower() in dict_commands:
#             command_message()
#         else:
#             usual_message()


while True:
    response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=5.21'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()
    # error requests.exceptions.ConnectionError: HTTPSConnectionPool(host='https', port=443): Max retries exceeded with url: //lp.vk.com/wh204074660?act=a_check&key=61fd4681a6acd72968d3fb0fea0784698cf6db34&ts=9&wait=25&mode=2&version=5.21 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000021DB59AE820>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
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
                    command_message(text, user_id, chat_id, vk)
                else:
                    usual_message(text, user_id, chat_id, vk, temp)

    data['ts'] = response['ts']  # обновление номера последнего обновления


# # Получаем лонгпул

