from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

import asyncio

api = '7387069503:AAFBg8T5xoI4N3HnvELstqzrd7pMpZWs2Ic'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == '/start')
async def start_message(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message()
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
