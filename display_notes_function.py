from datetime import datetime
import colorama
from colorama import Fore, Back, Style

colorama.init()


def display_notes(notes, level='full', sort_by=None, page_size=5):
    """
    Отображение списка заметок в удобном и понятном формате.

    :param notes: Список заметок (каждая заметка — это словарь)
    :param level: Уровень детализации ('full' — все поля, 'title_only' — только заголовки)
    :param sort_by: Поле для сортировки ('date_created' или 'deadline')
    :param page_size: Количество заметок на одну страницу при постраничном выводе
    """

    # Проверяем наличие заметок
    if not notes:
        print(Fore.RED + "У вас нет сохранённых заметок." + Style.RESET_ALL)
        return

    # Сортировка заметок по указанному полю
    if sort_by == 'date_created':
        sorted_notes = sorted(notes, key=lambda x: datetime.strptime(x['date_created'], '%d-%m-%Y'))
    elif sort_by == 'deadline':
        sorted_notes = sorted(notes, key=lambda x: datetime.strptime(x.get('deadline', '9999-99-99'), '%d-%m-%Y'))
    else:
        sorted_notes = notes

    # Постраничный вывод
    total_pages = len(sorted_notes) // page_size + (len(sorted_notes) % page_size > 0)
    current_page = 1

    while True:
        start_index = (current_page - 1) * page_size
        end_index = min(start_index + page_size, len(sorted_notes))

        for i in range(start_index, end_index):
            note = sorted_notes[i]

            print(Fore.GREEN + f"Заметка №{i + 1}:")
            if level == 'full':
                print(f"{Fore.YELLOW}Имя пользователя:{Style.RESET_ALL} {note['username']}")
                print(f"{Fore.YELLOW}Заголовок:{Style.RESET_ALL} {note['title']}")
                print(f"{Fore.YELLOW}Описание:{Style.RESET_ALL} {note['description']}")
                print(f"{Fore.YELLOW}Статус:{Style.RESET_ALL} {note['status']}")
                print(f"{Fore.YELLOW}Дата создания:{Style.RESET_ALL} {note['date_created']}")
                print(f"{Fore.YELLOW}Дедлайн:{Style.RESET_ALL} {note.get('deadline', '-')}")
            elif level == 'title_only':
                print(f"{Fore.YELLOW}Заголовок:{Style.RESET_ALL} {note['title']}")

            print('-' * 40)

        if current_page < total_pages:
            choice = input("Для перехода на следующую страницу нажмите Enter, для выхода введите 'q': ")
            if choice.lower() == 'q':
                break
            current_page += 1
        else:
            break


# Тестовый список заметок
notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю',
        'status': 'новая',
        'date_created': '27-11-2024',
        'deadline': '30-11-2024'
    },
    {
        'username': 'Мария',
        'title': 'Учеба',
        'description': 'Подготовиться к экзамену',
        'status': 'в процессе',
        'date_created': '25-11-2024',
        'deadline': '01-12-2024'
    }
]

# Вызов функции с различными параметрами
print("\nПолный вывод всех заметок:")
display_notes(notes)

print("\nТолько заголовки заметок:")
display_notes(notes, level='title_only')

print("\nСортировка по дате создания:")
display_notes(notes, sort_by='date_created')

print("\nСортировка по дедлайну:")
display_notes(notes, sort_by='deadline')