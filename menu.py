import math
import os
import re
from datetime import timedelta

from colorama import Fore, Style, Back, init

init(autoreset=True)


def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """Показать главное меню"""
    print(Fore.CYAN + "Меню действий:" + Style.RESET_ALL)
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Найти заметки")
    print("6. Выйти из программы")


def get_user_choice():
    """Получить выбор пользователя"""
    choice = input("\nВаш выбор: ")
    return choice


def validate_username(username):
    """
    Проверяет, является ли введённое имя пользователя допустимым.
    Имя пользователя должно состоять из двух частей (имя и фамилия),
    каждая часть должна начинаться с заглавной буквы и содержать минимум 2 символа.
    Разрешается использование букв русского алфавита, дефиса и пробела между частями.

    :param username: Имя пользователя.
    :return: True, если имя пользователя корректно, иначе False.
    """
    pattern = r'^([А-Я][а-я]+)\s+([А-Я][а-я]+)$'
    return bool(re.match(pattern, username))


def validate_date(date_str):
    """
    Проверяет, является ли строка допустимой датой в формате день-месяц-год.

    :param date_str: Строка с датой в формате день-месяц-год.
    :return: True, если дата валидна, иначе False.
    """
    try:
        # Пробуем преобразовать строку в объект datetime
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def get_default_issue_date():
    """
    Возвращает дату через одну неделю от текущей.

    :return: Дата через неделю в формате день-месяц-год.
    """
    today = datetime.now()
    default_date = today + timedelta(days=7)
    return default_date.strftime('%d-%m-%Y')


def create_note():
    """
    Запрашивает у пользователя информацию для создания заметки,
    проверяет введённые данные и возвращает заметку в виде словаря.

    :return: Словарь с полями заметки.
    """
    print("Создание новой заметки:")

    username = input("Введите имя пользователя (ФИО, например, Иван Иванов): ")
    while not validate_username(username):
        print(
            "Имя пользователя должно состоять из двух частей (имя и фамилия), каждая часть начинается с заглавной буквы.")
        username = input("Пожалуйста, введите корректное имя пользователя: ")

    title = input("Введите заголовок заметки: ")
    while not title.strip():  # Проверяем, что заголовок не пустой
        print("Заголовок не может быть пустым!")
        title = input("Пожалуйста, введите заголовок заметки: ")

    description = input("Введите описание заметки: ")
    while not description.strip():  # Проверяем, что описание не пустое
        print("Описание не может быть пустым!")
        description = input("Пожалуйста, введите описание заметки: ")

    status = input(
        f"Введите статус заметки (новая, в процессе, выполнена): ").lower()  # Приведение к нижнему регистру для унификации проверки

    while status not in ['новая', 'в процессе', 'выполнена']:
        print("Неверный статус! Попробуйте снова.")
        status = input(f"Введите статус заметки (новая, в процессе, выполнена): ").lower()

    current_date = datetime.now().strftime("%d-%m-%Y")

    deadline = input(
        f"Введите дату дедлайна (день-месяц-год), или оставьте пустым для использования даты по умолчанию ({get_default_issue_date()}): ")

    if not deadline.strip():  # Если пользователь оставил поле пустым, используем значение по умолчанию
        deadline = get_default_issue_date()
    else:
        while not validate_date(deadline):
            print("Неверный формат даты! Введите дату в формате день-месяц-год.")
            deadline = input(f"Введите дату дедлайна (день-месяц-год): ")

    note = {
        'username': username,
        'title': title,
        'description': description,
        'status': status.capitalize(),
        'date_created': current_date,
        'deadline': deadline
    }

    return note


def display_note(note, index):
    print(Fore.YELLOW + f'Заметка №{index}:')
    print(Fore.CYAN + f'Имя пользователя: {note["username"]}')
    print(Fore.GREEN + f'Заголовок: {note["title"]}')
    print(Fore.WHITE + f'Описание: {note["description"]}')
    print(Fore.BLUE + f'Статус: {note["status"]}')
    print(Fore.MAGENTA + f'Дата создания: {note["date_created"]}')
    print(Fore.MAGENTA + f'Дедлайн: {note["deadline"]}')
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
#-----------------------------------------------------

from datetime import datetime


def validate_issue_date(date_str):
    """
    Проверяет, является ли строка допустимой датой в формате день-месяц-год.
    :param date_str: Строка с датой
    :return: True, если дата валидна, иначе False
    """
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        print("Неверный формат даты! Пожалуйста, введите дату в формате день-месяц-год.")
        return False


def update_field(note, field_name, new_value):
    """
    Обновляет одно поле заметки и возвращает обновленный словарь.
    :param note: Словарь заметки
    :param field_name: Имя поля для обновления
    :param new_value: Новое значение для поля
    :return: Обновленную заметку
    """
    if field_name == 'issue_date' and not validate_issue_date(new_value):
        # Если дата введена неверно, возвращаем исходную заметку без изменений
        return note

    # Обновляем поле и возвращаем измененный словарь
    note[field_name] = new_value
    return note


def update_note(note):
    """
    Основная функция для обновления заметки.
    :param note: Словарь заметки
    :return: Обновленную заметку
    """
    global updated_note
    fields_to_update = {
        'username': 'Имя пользователя',
        'title': 'Заголовок',
        'content': 'Содержание',
        'status': 'Статус',
        'issue_date': 'Дата выпуска'
    }

    while True:
        print("\nТекущие данные заметки:")
        for key, value in note.items():
            print(f"{fields_to_update.get(key, key)}: {value}")

        print("\nКакие данные вы хотите обновить?")
        for key in fields_to_update.keys():
            print(f"- {key}")

        choice = input("Ваш выбор: ").strip().lower()

        if choice not in fields_to_update:
            print("Некорректное имя поля! Попробуйте еще раз.")
            continue

        new_value = input(f"Введите новое значение для {fields_to_update[choice]}: ")

        if new_value.strip() == "":
            print("Пустое значение! Поле останется прежним.")
            continue

        confirm = input(
            f"Вы уверены, что хотите обновить поле '{fields_to_update[choice]}'? (да/нет): ").strip().lower()
        if confirm != 'да':
            print("Отмена обновления!")
            continue

        updated_note = update_field(note, choice, new_value)
        break

    return updated_note


# Пример использования функции
try:
    note = {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    }

    updated_note = update_note(note)
    print("\nЗаметка обновлена:")
    for key, value in updated_note.items():
        print(f"{key.capitalize()}: {value}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
#-----------------------------------------------------

# Функция для вывода текущих заметок
def print_notes(notes):
    if not notes:
        print("Нет заметок.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['имя']}")
        print(f"   Заголовок: {note['заголовок']}")
        print(f"   Описание: {note['описание']}\n")


# Функция для удаления заметок по заданному критерию
def delete_note(notes, criterion, value):
    deleted_count = 0
    original_length = len(notes)

    # Перебираем заметки и удаляем те, которые соответствуют критерию
    notes[:] = [note for note in notes if note[criterion].lower() != value.lower()]

    # Выводим результат
    if len(notes) == original_length:
        print(f'Заметок с "{value}" не найдено.')
    else:
        deleted_count = original_length - len(notes)
        print(f"Удалено {deleted_count} заметок.")

    return notes


# Основная функция программы
def main():
    # Пример списка заметок
    notes = [
        {
            'имя': 'Алексей',
            'заголовок': 'Список покупок',
            'описание': 'Купить продукты на неделю'
        },
        {
            'имя': 'Мария',
            'заголовок': 'Учеба',
            'описание': 'Подготовиться к экзамену'
        }
    ]

    while True:
        print("\nВот текущий список ваших заметок:")
        print_notes(notes)

        # Запрашиваем у пользователя критерий для удаления
        choice = input("Что вы хотите сделать?\n"
                       "1. Удалить заметку по имени пользователя\n"
                       "2. Удалить заметку по заголовку\n"
                       "3. Завершить работу\n"
                       "Ваш выбор: ")

        if choice == '3':
            print("Завершение работы...")
            break

        elif choice == '1':
            user_name = input("Введите имя пользователя для удаления заметки: ").strip()
            notes = delete_note(notes, 'имя', user_name)

        elif choice == '2':
            title = input("Введите заголовок для удаления заметки: ").strip()
            notes = delete_note(notes, 'заголовок', title)

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

#-----------------------------------------------------

def format_note(note, index):
    """Форматирует одну заметку для вывода."""
    return f"""
Заметка №{index + 1}:
Имя пользователя: {note['username']}
Заголовок: {note['title']}
Описание: {note['content']}
Статус: {note['status']}"""


def print_search_results(results):
    """Выводит результат поиска в удобном формате."""
    if results:
        print("Найдены заметки:")
        for i, note in enumerate(results):
            print(format_note(note, i))
    else:
        print("Заметки, соответствующие запросу, не найдены.")


def search_notes(notes, keywords=None, status=None):
    """
    Функция для поиска заметок по списку ключевых слов и/или статусу.

    :param notes: список заметок
    :param keywords: список ключевых слов для поиска (необязательно)
    :param status: статус для фильтрации (необязательно)
    :return: список заметок, удовлетворяющих условиям поиска
    """
    # Проверяем наличие заметок
    if keywords is None:
        keywords = []
    if not notes:
        print("Список заметок пуст.")
        return []

    # Приводим ключевые слова к нижнему регистру
    lower_case_keywords = [keyword.lower() for keyword in keywords]

    # Фильтруем заметки по ключевым словам и статусу
    filtered_notes = []
    for note in notes:
        match_keywords = True
        match_status = True

        # Поиск по ключевым словам
        if lower_case_keywords:
            text_fields = [note['title'], note['content'], note['username']]
            match_keywords = all(
                any(keyword in field.lower() for field in text_fields)
                for keyword in lower_case_keywords
            )

        # Поиск по статусу
        if status is not None:
            match_status = note['status'].lower() == status.lower()

        # Добавляем заметку, если она подходит под все условия
        if match_keywords and match_status:
            filtered_notes.append(note)

    # Выводим результаты поиска
    print_search_results(filtered_notes)
    return filtered_notes

# Пример использования функции
notes = []  # Пустой список заметок

# Вызываем функцию с пустым списком заметок
print("\nПоиск по ключевым словам 'список' и 'купить':")
search_notes(notes, keywords=['список', 'купить '])

# Пример использования функции
notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'Новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    },
    {
        'username': 'Мария',
        'title': 'Учеба',
        'content': 'Подготовиться к экзамену',
        'status': 'В процессе',
        'created_date': '25-11-2024',
        'issue_date': '01-12-2024'
    },
    {
        'username': 'Иван',
        'title': 'План работы',
        'content': 'Завершить проект',
        'status': 'Выполнено',
        'created_date': '20-11-2024',
        'issue_date': '26-11-2024'
    }
]

# Примеры вызовов функции
print("\nПоиск по ключевым словам 'ПОКУПОК' и 'ПРОДУКТЫ':")
search_notes(notes, keywords=['ПОКУПОК', 'ПРОДУКТЫ'])

print("\nПоиск по ключевым словам 'СПОРТ' и 'КНИГИ':")
search_notes(notes, keywords=['СПОРТ', 'КНИГИ'])

print("\nПоиск по статусу 'в процессе':")
search_notes(notes, status='в процессе')

print("\nПоиск по ключевым словам 'РАБОТЫ' и статусу 'выполнено':")
search_notes(notes, keywords=['РАБОТЫ'], status='выполнено')

#-----------------------------------------------------
def main():
    """Главная функция программы"""
    notes = []  # Список для хранения заметок
    while True:
        clear_screen()
        show_menu()
        try:
            choice = int(get_user_choice())
            if choice == 1:
                new_note = create_note()
                notes.append(new_note)
                print(Fore.GREEN + "\nНовая заметка создана!" + Style.RESET_ALL)
            elif choice == 2:
                display_notes(notes)
            elif choice == 3:
                if notes:
                    display_notes(notes)
                    update_note(notes)
                else:
                    print(Fore.RED + "\nНет заметок для обновления." + Style.RESET_ALL)
            elif choice == 4:
                if notes:
                    display_notes(notes)
                    delete_note(notes)
                else:
                    print(Fore.RED + "\nНет заметок для удаления." + Style.RESET_ALL)
            elif choice == 5:
                if notes:
                    search_notes(notes)
                else:
                    print(Fore.RED + "\nНет заметок для поиска." + Style.RESET_ALL)
            elif choice == 6:
                print(Fore.MAGENTA + "\nПрограмма завершена. Спасибо за использование!" + Style.RESET_ALL)
                break
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + "\nНеверный выбор. Пожалуйста, выберите действие из списка." + Style.RESET_ALL)
            input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()