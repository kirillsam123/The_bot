import json
import os


SCHEDULE_FILE = 'Datebase/schedule.json'


def load_schedule():
    """Загрузка расписания из файла"""
    if not os.path.exists(SCHEDULE_FILE):
        print("Файл расписания не найден!")
        return None
    
    with open(SCHEDULE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
    

def save_schedule(data):
    """Сохранение расписания в файл"""
    with open(SCHEDULE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def show_schedule():
    """Показать расписание на выбранный день"""
    schedule = load_schedule()
    if not schedule:
        return
    
    days = {
        '1': 'monday',
        '2': 'tuesday', 
        '3': 'wednesday',
        '4': 'thursday',
        '5': 'friday'
    }
    
    print("\n--- Просмотр расписания ---")
    print("1 - Понедельник")
    print("2 - Вторник")
    print("3 - Среда")
    print("4 - Четверг")
    print("5 - Пятница")
    print("6 - Вся неделя")
    
    choice = input("Выберите день или 6 для всей недели: ")
    
    if choice == '6':
        show_week_schedule(schedule)
    elif choice in days:
        show_day_schedule(schedule, days[choice])
    else:
        print("Неверный выбор!")

def show_day_schedule(schedule, day):
    """Показать расписание на конкретный день"""
    day_names = {
        'monday': 'Понедельник',
        'tuesday': 'Вторник',
        'wednesday': 'Среда', 
        'thursday': 'Четверг',
        'friday': 'Пятница'
    }
    
    print(f"\n--- Расписание на {day_names[day]} ---")
    lessons = schedule['week'][day]
    
    if not lessons:
        print("Уроков нет!")
        return
    
    for lesson in lessons:
        print(f"{lesson['number']}. {lesson['time']} - {lesson['subject']}")
        print(f"   Учитель: {lesson['teacher']}")
        print(f"   Кабинет: {lesson['room']}")
        print()

def show_week_schedule(schedule):
    """Показать расписание на всю неделю"""
    print(f"\n--- Расписание на неделю ({schedule['school']}) ---")
    
    for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        show_day_schedule(schedule, day)

def add_lesson():
    """Добавить урок в расписание"""
    schedule = load_schedule()
    if not schedule:
        return
    
    print("\n--- Добавление урока ---")
    
    days = {
        '1': 'monday',
        '2': 'tuesday',
        '3': 'wednesday',
        '4': 'thursday', 
        '5': 'friday'
    }
    
    print("Выберите день:")
    for key, day in days.items():
        print(f"{key} - {day}")
    
    day_choice = input("День: ")
    if day_choice not in days:
        print("Неверный выбор дня!")
        return
    
    selected_day = days[day_choice]
    
    # Получаем следующий номер урока
    lessons = schedule['week'][selected_day]
    next_number = max([lesson['number'] for lesson in lessons], default=0) + 1
    
    print(f"\nДобавление урока #{next_number}")
    subject = input("Предмет: ")
    teacher = input("Учитель: ")
    room = input("Кабинет: ")
    time = input("Время (например, 8:30-9:15): ")
    
    new_lesson = {
        "number": next_number,
        "subject": subject,
        "teacher": teacher,
        "room": room,
        "time": time
    }
    
    schedule['week'][selected_day].append(new_lesson)
    save_schedule(schedule)
    print("Урок успешно добавлен!")

def delete_lesson():
    """Удалить урок из расписания"""
    schedule = load_schedule()
    if not schedule:
        return
    
    print("\n--- Удаление урока ---")
    
    days = {
        '1': 'monday',
        '2': 'tuesday',
        '3': 'wednesday',
        '4': 'thursday',
        '5': 'friday'
    }
    
    print("Выберите день:")
    for key, day in days.items():
        print(f"{key} - {day}")
    
    day_choice = input("День: ")
    if day_choice not in days:
        print("Неверный выбор дня!")
        return
    
    selected_day = days[day_choice]
    lessons = schedule['week'][selected_day]
    
    if not lessons:
        print("В этот день нет уроков!")
        return
    
    show_day_schedule(schedule, selected_day)
    
    try:
        lesson_number = int(input("Введите номер урока для удаления: "))
    except ValueError:
        print("Номер урока должен быть числом!")
        return
    
    # Удаляем урок
    initial_count = len(lessons)
    schedule['week'][selected_day] = [lesson for lesson in lessons if lesson['number'] != lesson_number]
    
    if len(schedule['week'][selected_day]) < initial_count:
        # Перенумеровываем оставшиеся уроки
        for i, lesson in enumerate(schedule['week'][selected_day], 1):
            lesson['number'] = i
        
        save_schedule(schedule)
        print("Урок успешно удален!")
    else:
        print("Урок с таким номером не найден!")

def find_teacher_lessons():
    """Найти все уроки учителя"""
    schedule = load_schedule()
    if not schedule:
        return
    
    print("\n--- Поиск уроков учителя ---")
    teacher = input("Введите фамилию учителя: ")
    
    found_lessons = []
    
    for day in schedule['week']:
        for lesson in schedule['week'][day]:
            if teacher.lower() in lesson['teacher'].lower():
                found_lessons.append({
                    'day': day,
                    'lesson': lesson
                })
    
    if not found_lessons:
        print(f"Уроки учителя {teacher} не найдены!")
        return
    
    day_names = {
        'monday': 'Понедельник',
        'tuesday': 'Вторник',
        'wednesday': 'Среда',
        'thursday': 'Четверг',
        'friday': 'Пятница'
    }
    
    print(f"\n--- Уроки учителя {teacher} ---")
    for item in found_lessons:
        lesson = item['lesson']
        day = day_names[item['day']]
        print(f"{day}, {lesson['time']} - {lesson['subject']} (каб. {lesson['room']})")

def main():
    """Основное меню программы"""
    while True:
        print("\n=== Управление расписанием ===")
        print("1. Показать расписание")
        print("2. Добавить урок")
        print("3. Удалить урок")
        print("4. Найти уроки учителя")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            show_schedule()
        elif choice == '2':
            add_lesson()
        elif choice == '3':
            delete_lesson()
        elif choice == '4':
            find_teacher_lessons()
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

