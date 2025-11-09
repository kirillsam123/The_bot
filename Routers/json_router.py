from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from Datebase.json_bot import (
    get_day_schedule,
    get_week_schedule,
    get_en_day,
    get_ru_day
)


json_router = Router()


def create_scheduler_text(lessons: dict) -> str:
    res: str = ''
    for lesson in lessons:
        res += f"{lesson['number']}. {lesson['time']} - {lesson['subject']}\n" \
            + f"    Учитель: {lesson['teacher']}\n" \
            + f"    Кабинет: {lesson['room']}\n"
    return res


@json_router.message(Command(commands='расписание', prefix='/'))
async def shedule(message: Message) -> None:
    day: str = message.text.split(" ")[1]

    if day.lower() == 'неделя':
        answer: str = ''
        t = get_week_schedule()
        for d, s in t.items():
            answer += f'{get_ru_day(d)}\n'
            answer += create_scheduler_text(s)
            answer += '\n'
        await message.reply(text=answer)
    else:
        t = get_en_day(day)
        if t == '':
            await message.reply(
                text='Ошибка такого дня недели нет в расписнии'
            )
        else:
            s = create_scheduler_text(get_day_schedule(day=t))
            await message.reply(text=s)

