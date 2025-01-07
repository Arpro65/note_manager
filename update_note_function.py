import re
from datetime import datetime


def validate_issue_date(date_str):
    """
    Проверка формата даты 'день-месяц-год'.
    Возвращает True, если дата валидна, иначе False.
    """
    date_pattern = r'^\d{2}-\d{2}-\d{4}$'
    if not re.match(date_pattern, date_str):
        return False

    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def update_field(note, field_name, new_value):
    """
    Обновление указанного поля заметки.
    """
    if field_name == 'issue_date':
        # Проверяем формат даты
        if not validate_issue_date(new_value):
            print("Некорректный формат даты! Введите дату в формате 'день-месяц-год'.")
            return note

    note[field_name] = new_value
    return note


def get_user_choice():
    """
    Запрашиваем у пользователя выбор поля для обновления.
    """
    while True:
        choice = input("\nКакое поле вы хотите обновить?\n"
                       "1. username\n"
                       "2. title\n"
                       "3. content\n"
                       "4. status\n"
                       "5. issue_date\n"
                       "Введите номер поля: ")

        if choice in ['1', '2', '3', '4', '5']:
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    return int(choice)


def get_new_value(field_name):
    """
    Получаем новое значение от пользователя.
    """
    if field_name == 'issue_date':
        while True:
            value = input(f"Введите новую дату ({field_name}) в формате 'день-месяц-год': ")
            if validate_issue_date(value):
                break
            else:
                print("Некорректная дата. Пожалуйста, попробуйте еще раз.")
    else:
        value = input(f"Введите новое значение для поля '{field_name}': ")

    return value


def confirm_update():
    """
    Подтверждение обновления поля.
    """
    while True:
        confirmation = input("Вы уверены, что хотите обновить поле? (да/нет): ").lower()
        if confirmation in ['да', 'нет']:
            break
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")

    return confirmation == 'да'


def update_note(note):
    """
    Основная функция для обновления заметки.
    Принимает заметку (словарь), позволяет пользователю выбрать поле для обновления,
    запрашивает новое значение и обновляет выбранное поле.
    """
    fields = {
        1: 'username',
        2: 'title',
        3: 'content',
        4: 'status',
        5: 'issue_date'
    }

    print("\nТекущие данные заметки:")
    for key, value in note.items():
        print(f"{key}: {value}")

    choice = get_user_choice()
    field_name = fields[choice]

    new_value = get_new_value(field_name)

    if confirm_update():
        updated_note = update_field(note, field_name, new_value)
        print(f"Поле '{field_name}' успешно обновлено!")
    else:
        print("Отмена обновления.")
        updated_note = note

    return updated_note


# Пример использования функции
if __name__ == "__main__":
    note = {
        'username': 'Иван Иванов',
        'title': 'Заметка о работе',
        'content': 'Описание задачи.',
        'status': 'Новая',
        'issue_date': '01-10-2023'
    }

    updated_note = update_note(note)
    print("\nОбновленная заметка:")
    for key, value in updated_note.items():
        print(f"{key}: {value}")