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