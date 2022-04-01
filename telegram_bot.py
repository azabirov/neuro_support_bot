import logging
import os

from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dialogflow_detect_intent import detect_intent_text

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуйте {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def reply_neural(update: Update, context: CallbackContext) -> None:
    reply = detect_intent_text(
        project_id=os.environ.get("PROJECT_ID"),
        session_id=f"tgbot-{os.environ.get('PROJECT_ID')}",
        text=update.message.text,
        language_code="ru",
    )
    update.message.reply_text(reply)


def main() -> None:
    load_dotenv()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    updater = Updater(os.environ.get("TELEGRAM_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_neural))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
