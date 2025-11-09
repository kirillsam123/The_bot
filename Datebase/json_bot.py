import json
import os 


SCHEDULE_FILE: str = 'Datebase/schedule.json'
DAYS = {
    '1': 'monday',
    '2': 'tuesday', 
    '3': 'wednesday',
    '4': 'thursday',
    '5': 'friday'
}


def get_en_day(day: str) -> str:
    day_names = {
        'понедельник': 'monday',
        'вторник': 'tuesday',
        'среда': 'wednesday',
        'четверг': 'thursday',
        'пятница': 'friday',
        'суббота': 'saturday'
    }
    day = day.lower()
    if day in day_names.keys():
        return day_names[day.lower()]
    else:
        return ''


def get_ru_day(day: str) -> str:
    day_names = {
        'monday': 'понедельник',
        'tuesday': 'вторник',
        'wednesday': 'среда',
        'thursday': 'четверг',
        'friday': 'пятница',
        'saturday': 'суббота'
    }
    day = day.lower()
    if day in day_names.keys():
        return day_names[day.lower()]
    else:
        return ''


def load_schedule() -> dict:
    """Загрузка расписания из файла"""
    if not os.path.exists(SCHEDULE_FILE):
        return {}
    
    with open(SCHEDULE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_day_schedule(day: str) -> dict:
    """Показать расписание на конкретный день"""
    schedule: dict = load_schedule()
    if not schedule:
        return {}

    lessons: dict = schedule['week'][day]
    if not lessons:
        return {}
    
    return lessons


def get_week_schedule() -> list[dict]:
    """Показать расписание на всю неделю"""
    schedule = load_schedule()
    if not schedule:
        return []
    return schedule['week']