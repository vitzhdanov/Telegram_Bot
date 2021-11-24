from aiogram import types
from aiogram.dispatcher import filters
from loader import dp
import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

SHORTNER_WORD = ['Бот', 'обреж', 'ссылку']


# укорачивает ссылку
@dp.message_handler(filters.Text(contains=SHORTNER_WORD))
async def test(message: types.Message):
    user_link = message.text.replace('Бот обреж ссылку ', '').replace('@zed_is_dead_bot', '')
    resp = requests.post('https://www.iclc.info/shortner/', {'long_url': str(user_link)}).json()
    sym = resp['short_sym']
    em = resp['short_em']
    await message.answer(f"{sym}\n\n{em}")
