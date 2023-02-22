from dotenv import dotenv_values
import logging
import pickle
import random
import face_recognition as fr
import tqdm
from PIL import Image
import io
import time
import hashlib
import os
import re


from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler, CallbackQueryHandler
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hi! To generate new cat planet, type /random_cat')


async def get_random_cat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_document(document=open('aa.gif', 'rb'))


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
