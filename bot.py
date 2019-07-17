from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import vk_api
import random
from t import token, group
from time import sleep

vk = vk_api.VkApi(token=token()) # token() - получать в разделе "Работа с API" -> Ключ доступа
vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, group()) # group() - id группы

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id == event.object.from_id:
                    try:
                        track = event.object.attachments[0]['audio']['artist'] + ' - ' + event.object.attachments[0]['audio']['title']
                        url = event.object.attachments[0]['audio']['url'].split('?')[0]
                        vk.method('messages.send', {'peer_id': event.object.from_id, 'message': '🎵 Трек: ' + track + '\n💾 Ссылка для скачивания:\n' + url, 'random_id': random.randint(-2147483648, 2147483647)})
                    except:
                        vk.method('messages.send', {'peer_id': event.object.from_id, 'message': 'Отправь аудиозапись, чтобы получить ссылку на скачивание', 'random_id': random.randint(-2147483648, 2147483647)})
    except Exception as e:
        print(e)
        sleep(3)

