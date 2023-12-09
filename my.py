import vk_api
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = ""
vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

vars = ['камень', 'ножницы', 'бумага']


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower() in vars:
        if event.from_user:
            user = event.text.lower()
            bot = choice(vars)
            vk.messages.send(user_id = event.user_id, message = bot, random_id=randrange(0, 3))
            out = None
            if bot == 'ножницы':
                if user == 'ножницы':
                    out = 'Ничья'
                elif user == 'бумага':
                    out = 'Ты проиграл'
                else:
                    out = 'Ты выйграл'
            elif bot == 'бумага':
                if user == 'ножницы':
                    out = 'Ты выйграл'
                elif user == 'бумага':
                    out ='Ничья'
                else:
                    out = 'Ты проиграл'
            else:
                if user =='ножницы':
                    out = 'Ты проиграл'
                elif user == 'бумага':
                    out = 'Ты выйграл'
                else:
                    out ='Ничья'
            vk.messages.send(user_id = event.user_id, message = out, random_id=randrange(0, 3))
