import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from dotenv import load_dotenv
import random
from bot import detect_intent_text


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1,1000)
    )


def neural_reply_vk(event, vk_api):
    message=detect_intent_text(
            project_id=os.environ.get("PROJECT_ID"),
            session_id=os.environ.get("PROJECT_ID"),
            text=event.text,
            language_code="ru",
            ignore_fallback=True
    )
    if message:
        vk_api.messages.send(
            user_id=event.user_id,
            message=message,
            random_id=random.randint(1, 1000)
        )

load_dotenv()

if __name__ == "__main__":
    vk_session = vk_api.VkApi(token=os.environ.get("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            if event.to_me:
                neural_reply_vk(event, vk_api)
                print('Для меня от: ', event.user_id)
            else:
                print('От меня для: ', event.user_id)
            print('Текст:', event.text)