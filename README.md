# Бот для работы с клиентами

Бот отрабатывающий сценарии из DialogFlow.

Для установки всех необходимых библиотек 
используйте `pip install -r requirements.txt` в командной строке

Необходимо создать в папке проекта `.env` файл содержаший в себе значения:

```
CHAT_ID = ID чата в Telegram
ADMIN_CHAT_ID = ID часа с админом в Telegram
TELEGRAM_TOKEN = Токен бота Telegram
PROJECT_ID = ID проекта на DialogFlow
GOOGLE_APPLICATION_CREDENTIALS = Путь файла с ключами Google
VK_TOKEN = Токен группы или сообщества ВК
```