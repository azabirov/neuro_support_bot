import logging
import os

from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google.cloud import dialogflow

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуйте {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def neural_reply(update: Update, context: CallbackContext) -> None:
    reply = detect_intent_text(
        project_id=os.environ.get("PROJECT_ID"),
        session_id=os.environ.get("PROJECT_ID"),
        text=update.message.text,
        language_code="ru",
    )
    update.message.reply_text(reply)


def detect_intent_text(project_id, session_id, text, language_code, ignore_fallback=False):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    if ignore_fallback and response.query_result.intent.is_fallback:
        return None

    return response.query_result.fulfillment_text


def main() -> None:
    load_dotenv()
    updater = Updater(os.environ.get("TELEGRAM_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, neural_reply))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
