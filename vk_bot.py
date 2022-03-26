import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from dotenv import load_dotenv
import random
from telegram_bot import detect_intent_text


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1,1000)
    )


def reply_vk(event, vk_api):
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


if __name__ == "__main__":
    load_dotenv()

    vk_session = vk_api.VkApi(token=os.environ.get("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                reply_vk(event, vk_api)
