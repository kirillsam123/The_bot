from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

main_router = Router()


# Handler on command /start
@main_router.message(Command(commands='start', prefix='/'))
async def start_command(message: Message) -> None:
    welcome_text: str = "👋 Привет! Я бот!"
    await message.answer(welcome_text)


@main_router.message(F.text == '```СНЕГРОВИК```')
async def test(message: Message) -> None:
    await message.answer(
        text='test by bot'
    )


@main_router.message(F.photo)
async def photo_info(message: Message) -> None:
    t = f'''
Message ID: {message.message_id}\n
Date: {message.date.strftime(format='%d/%m/%Y, %H:%M:%S')}\n
Chat: {message.chat}\n
Sender chat: {message.sender_chat}\n
From user: {message.from_user}\n
Photo: {message.photo}\n
Audio: {message.audio}\n
Video: {message.video}\n
Sticker: {message.sticker}\n
'''
    await message.reply(
        text=t
    )


@main_router.message(F.text == "dict")
async def d(message: Message) -> None:
    d = {
        "body": [1, 2, 3],
        "head": {
            "1": 1,
            "2": 2
        }
    }
    await message.answer(
        text=["head"] ["1"]
    )
    await message.answer(
        text=["head"] ["2s"]
    )

