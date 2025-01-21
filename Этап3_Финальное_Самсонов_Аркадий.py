import os
import re
from datetime import datetime, timedelta
from colorama import Fore, Style, Back, init

init(autoreset=True)

# Пример заметок
notes = [
    {
        'Имя пользователя': 'Алексей',
        'Заголовок': 'Список покупок',
        'Описание': 'Купить продукты на неделю',
        'Статус': 'Новая',
        'Дата создания': '27-11-2024',
        'Дата дедлайна': '30-11-2024'
    },
    {
        'Имя пользователя': 'Мария',
        'Заголовок': 'Учеба',
        'Описание': 'Подготовиться к экзамену',
        'Статус': 'В процессе',
        'Дата создания': '25-11-2024',
        'Дата дедлайна': '01-12-2024'
    },
    {
        'Имя пользователя': 'Иван',
        'Заголовок': 'План работы',
        'Описание': 'Завершить проект',
        'Статус': 'Выполнено',
        'Дата создания': '20-11-2024',
        'Дата дедлайна': '26-11-2024'
    }
]

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Показать главное меню"""
    print(Fore.CYAN + "\nМеню действий:" + Style.RESET_ALL)
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Найти заметки")
    print("6. Выйти из программы")

def get_user_choice():
    """Получить выбор пользователя"""
    return input("\nВаш выбор: ")

def validate_username(username):
    """
    Проверяет имя пользователя: Имя и Фамилия с заглавной буквы
    """
    pattern = r'^([А-ЯЁ][а-яё]+)\s+([А-ЯЁ][а-яё]+)$'
    return bool(re.match(pattern, username))

def validate_issue_date(date_str):
    """
    Проверяет корректность даты в формате 'день-месяц-год'
    """
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def get_default_issue_date():
    """
    Возвращает дату через неделю
    """
    return (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')

def create_note():
    """Создаёт новую заметку"""
    while True:
        username = input("Введите имя пользователя (ФИО): ")
        if validate_username(username):
            break
        print(Fore.RED + "Имя пользователя должно состоять из двух слов с заглавной буквы." + Style.RESET_ALL)

    title = input("Введите заголовок заметки: ").strip()
    while not title:
        title = input(Fore.RED + "Заголовок не может быть пустым. Повторите ввод: " + Style.RESET_ALL).strip()

    description = input("Введите описание заметки: ").strip()
    while not description:
        description = input(Fore.RED + "Описание не может быть пустым. Повторите ввод: " + Style.RESET_ALL).strip()

    status = input("Введите статус заметки (новая, в процессе, выполнена): ").lower()
    while status not in ['новая', 'в процессе', 'выполнена']:
        status = input(Fore.RED + "Некорректный статус! Повторите ввод: " + Style.RESET_ALL).lower()

    current_date = datetime.now().strftime("%d-%m-%Y")
    deadline = input(f"Введите дату дедлайна (или нажмите Enter для даты по умолчанию {get_default_issue_date()}): ").strip()
    if not deadline:
        deadline = get_default_issue_date()
    else:
        while not validate_issue_date(deadline):
            deadline = input(Fore.RED + "Некорректный формат даты! Повторите ввод (дд-мм-гггг): " + Style.RESET_ALL).strip()

    return {
        'Имя пользователя': username,
        'Заголовок': title,
        'Описание': description,
        'Статус': status.capitalize(),
        'Дата создания': current_date,
        'Дата дедлайна': deadline
    }

def display_notes(notes, page_size=5):
    """Выводит список заметок с постраничной навигацией"""
    if not notes:
        print(Fore.RED + "Нет заметок для отображения." + Style.RESET_ALL)
        return

    notes = sorted(notes, key=lambda x: datetime.strptime(x['Дата создания'], '%d-%m-%Y'))
    total_pages = (len(notes) + page_size - 1) // page_size

    current_page = 1
    while True:
        start = (current_page - 1) * page_size
        end = start + page_size
        for i, note in enumerate(notes[start:end], start=start + 1):
            print(Fore.YELLOW + f"\nЗаметка №{i}")
            for key, value in note.items():
                print(Fore.CYAN + f"{key}: {value}" + Style.RESET_ALL)

        command = input(f"\nСтраница {current_page}/{total_pages} (н - следующая, п - предыдущая, в - выход): ").lower()
        if command == 'н' and current_page < total_pages:
            current_page += 1
        elif command == 'п' and current_page > 1:
            current_page -= 1
        elif command == 'в':
            break
        else:
            print(Fore.RED + "Неверная команда!" + Style.RESET_ALL)


def update_note():
    """Обновить заметку"""
    display_notes(notes)
    try:
        note_index = int(input("\nВведите номер заметки для обновления: ")) - 1
        if 0 <= note_index < len(notes):
            note = notes[note_index]
            print(Fore.CYAN + f"Обновляем заметку: {note['Заголовок']}" + Style.RESET_ALL)

            title = input("Введите новый заголовок (или Enter для сохранения текущего): ").strip()
            if title:
                note['Заголовок'] = title

            description = input("Введите новое описание (или Enter для сохранения текущего): ").strip()
            if description:
                note['Описание'] = description

            status = input(
                "Введите новый статус (новая, в процессе, выполнена, или Enter для сохранения текущего): ").lower()
            if status in ['новая', 'в процессе', 'выполнена']:
                note['Статус'] = status.capitalize()

            deadline = input("Введите новую дату дедлайна (дд-мм-гггг, или Enter для сохранения текущей): ").strip()
            if deadline and validate_issue_date(deadline):
                note['Дата дедлайна'] = deadline

            print(Fore.GREEN + "Заметка успешно обновлена!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Заметка с таким номером не найдена!" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Некорректный ввод! Ожидается номер заметки." + Style.RESET_ALL)


def delete_note():
    """Удалить заметку"""
    display_notes(notes)
    try:
        note_index = int(input("\nВведите номер заметки для удаления: ")) - 1
        if 0 <= note_index < len(notes):
            deleted_note = notes.pop(note_index)
            print(Fore.GREEN + f"Заметка '{deleted_note['Заголовок']}' успешно удалена!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Заметка с таким номером не найдена!" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Некорректный ввод! Ожидается номер заметки." + Style.RESET_ALL)


def search_notes():
    """Найти заметки по критериям"""
    search_query = input("Введите ключевое слово для поиска (в заголовке или описании): ").strip().lower()
    results = [note for note in notes if
               search_query in note['Заголовок'].lower() or search_query in note['Описание'].lower()]
    if results:
        print(Fore.GREEN + f"Найдено {len(results)} заметок:" + Style.RESET_ALL)
        display_notes(results)
    else:
        print(Fore.RED + "По вашему запросу ничего не найдено." + Style.RESET_ALL)


def main():
    while True:
        clear_screen()
        show_menu()
        choice = get_user_choice().strip()

        if choice == '1':
            notes.append(create_note())
            print(Fore.GREEN + "\nЗаметка успешно создана!" + Style.RESET_ALL)
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes()
        elif choice == '6':
            print(Fore.MAGENTA + "\nПрограмма завершена." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nНекорректный выбор!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()