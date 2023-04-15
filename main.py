"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('uz')

API_TOKEN = '6021948978:AAFPHEffypO1FzN_uU1o0tW5fQ5uz6loaNk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!")



@dp.message_handler()
async def bot(message: types.Message):

  try:
      respond = wikipedia.summary(message.text)
      await message.answer(respond)
  except:
      await message.answer("Bu navzuga doir maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)