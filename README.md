# Бот для работы с клиентами

Бот отрабатывающий сценарии из DialogFlow.

### Как установить 

Для установки всех необходимых библиотек 
используйте `pip install -r requirements.txt` в командной строке

Необходимо создать в папке проекта `.env` файл содержаший в себе значения:

```
CHAT_ID = <ID чата в Telegram>
ADMIN_CHAT_ID = <ID часа с админом в Telegram>
TELEGRAM_TOKEN = <Токен бота Telegram>
PROJECT_ID = <ID проекта на DialogFlow>
GOOGLE_APPLICATION_CREDENTIALS = <Путь файла с ключами Google>
VK_TOKEN = <Токен группы или сообщества VK>
```

Для того, чтобы создать intent в DialogFlow, при наличии JSON файла с данными
воспользуйте скриптом `create_intent` с помощью команды `python create_intent <ссылка на JSON файл с данными>`

### Цель проекта:
Создать ботов в Telegram и VK способных обрабатывать запросы с помощью DialogFlow.