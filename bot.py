from aiogram import executor
from dispatcher import dp
import handlers

from db import BotDB
BotDB = BotDB('users_test.db')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)