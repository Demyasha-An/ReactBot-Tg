import asyncio
import random
import logging
import aiogram.filters
from spisok import *
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandObject
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token='token')
dp = Dispatcher()

@dp.message(Command('start', 'help'))
async def help(message: types.Message):
    await message.answer('Привет, я React.\nБот который может делать прекольные штуки.\nЧто бы посмотреть список команд пропиши команду /list')

@dp.message(Command('list'))
async def list(message: types.Message):
    await message.answer('Весь список команд:\n/shot - выстрел \n/sleep - сон \n/hug - обнять \n/bite - укусить \n/kiss - поцеловать\n/slap - ударить\n/love - признятся в любви\n\
/sad - грустить\n/eat - кушать\n/stroke - погладить\n/topple - завалить на кровать\n/lick - лизнуть\n')

@dp.message(Command("shot"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, убил одним выстрелом {command.args}\n {random.choice(text_shot)}")
        await bot.send_animation(animation=random.choice(url_shot), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя того, в кого хочешь выстрелить!")

@dp.message(Command("sleep"))
async def cmd_name(message: types.Message, command: CommandObject):
    await message.answer(f"@{message.from_user.username}, спит, давайте потише.")
    await bot.send_animation(animation=random.choice(url_sleep), chat_id=message.chat.id)

@dp.message(Command("hug"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, обнял {command.args}\n {random.choice(text_hug)}")
        await bot.send_animation(animation=random.choice(url_hug), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кого хочешь обнять!")

@dp.message(Command("bite"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, укусил {command.args}\n {random.choice(text_bite)}")
        await bot.send_animation(animation=random.choice(url_bite), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кого хочешь укусить!")

@dp.message(Command("kiss"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, поцеловал {command.args}\n {random.choice(text_kiss)}")
        await bot.send_animation(animation=random.choice(url_kiss), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кого хочешь поцеловать!")

@dp.message(Command("slap"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, ударил {command.args}\n {random.choice(text_slap)}")
        await bot.send_animation(animation=random.choice(url_slap), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кого хочешь ударить!")

@dp.message(Command("love"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, признался в любви  {command.args}\n {random.choice(text_love)}")
        await bot.send_animation(animation=random.choice(url_love), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кому хочешь признаться в любви!")

@dp.message(Command("sad"))
async def cmd_name(message: types.Message, command: CommandObject):
    await message.answer(f"@{message.from_user.username}, грустит.\n{random.choice(text_sad)}")
    await bot.send_animation(animation=random.choice(url_sad), chat_id=message.chat.id)

@dp.message(Command("eat"))
async def cmd_name(message: types.Message, command: CommandObject):
    await message.answer(f"@{message.from_user.username}, кушает.\n {random.choice(text_eat)}")
    await bot.send_animation(animation=random.choice(url_eat), chat_id=message.chat.id)

@dp.message(Command("stroke"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, погладил {command.args}\n {random.choice(text_stroke)}")
        await bot.send_animation(animation=random.choice(url_stroke), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кого хочешь погладить!")

@dp.message(Command("topple"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, завалил на кровать  {command.args}\n {random.choice(text_topple)}")
        await bot.send_animation(animation=random.choice(url_topple), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя/ник того, кого хочеш завалить на кровать!")

@dp.message(Command("lick"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"@{message.from_user.username}, лизнул {command.args}\n {random.choice(text_lick)}")
        await bot.send_animation(animation=random.choice(url_lick), chat_id=message.chat.id)
    else:
        await message.answer("Укажи имя того, кого хочеш лизнуть!")

async def main():
    await dp.start_polling(bot)

if __name__ =='__main__':
    asyncio.run(main())