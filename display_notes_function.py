from datetime import datetime
import math
from colorama import Fore, Back, Style, init

init(autoreset=True)


def display_note(note, index):
    print(Fore.YELLOW + f'Заметка №{index}:')
    print(Fore.CYAN + f'Имя пользователя: {note["username"]}')
    print(Fore.GREEN + f'Заголовок: {note["title"]}')
    print(Fore.WHITE + f'Описание: {note["description"]}')
    print(Fore.BLUE + f'Статус: {note["status"]}')
    print(Fore.MAGENTA + f'Дата создания: {note["date_created"].strftime("%d-%m-%Y")}')
    print(Fore.MAGENTA + f'Дедлайн: {note["deadline"].strftime("%d-%m-%Y")}')
    print(Back.BLACK + '-' * 40 + Style.RESET_ALL)


def display_notes(notes, page_size=5):
    if not notes:
        print(Fore.RED + "У вас нет сохранённых заметок." + Style.RESET_ALL)
        return

    sorted_notes = sorted(notes, key=lambda note: note.get('date_created', ''))

    total_pages = math.ceil(len(sorted_notes) / page_size)
    current_page = 1

    while True:
        start_index = (current_page - 1) * page_size
        end_index = min(start_index + page_size, len(sorted_notes))

        for index, note in enumerate(sorted_notes[start_index:end_index], start=start_index + 1):
            display_note(note, index)

        try:
            choice = input(
                '\n' + Fore.YELLOW + f'Страница {current_page}/{total_pages}. Введите "н" для следующей страницы, "п" для предыдущей или "в" для выхода: ' + Style.RESET_ALL).lower()

            if choice == 'н':
                if current_page < total_pages:
                    current_page += 1
            elif choice == 'п':
                if current_page > 1:
                    current_page -= 1
            elif choice == 'в':
                break
            else:
                print(Fore.RED + "Неверная команда. Попробуйте снова." + Style.RESET_ALL)
        except KeyboardInterrupt:
            print("\nПрервано пользователем.")
            break

    print(Fore.GREEN + "Вы вышли из просмотра заметок." + Style.RESET_ALL)


# Тестовый список заметок
notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "description": "Купить продукты на неделю",
        "status": "новая",
        "date_created": datetime.strptime("27-11-2024", "%d-%m-%Y"),
        "deadline": datetime.strptime("30-11-2024", "%d-%m-%Y")
    },
    {
        "username": "Мария",
        "title": "Учеба",
        "description": "Подготовиться к экзамену",
        "status": "в процессе",
        "date_created": datetime.strptime("25-11-2024", "%d-%m-%Y"),
        "deadline": datetime.strptime("01-12-2024", "%d-%m-%Y")
    }
]

# Вызов функции
display_notes(notes)