import logging

from dotenv import dotenv_values
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from model.generator import generate_image

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hi! To generate new cat planet, type /random_cat')


async def get_random_cat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    image_path = generate_image()
    await update.message.reply_document(document=open(image_path, 'rb'))


def main() -> None:
    application = Application.builder().token(
        dotenv_values(".env")['BOT_TOKEN']).build()

    start_handler = CommandHandler('start', start)
    random_cat_handler = CommandHandler('random_cat', get_random_cat)

    application.add_handler(random_cat_handler)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
