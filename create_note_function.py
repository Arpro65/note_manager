import re
from datetime import datetime
from datetime import timedelta


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

    content = input("Введите описание заметки: ")
    while not content.strip():  # Проверяем, что описание не пустое
        print("Описание не может быть пустым!")
        content = input("Пожалуйста, введите описание заметки: ")

    status = input(
        f"Введите статус заметки (новая, в процессе, выполнена): ").lower()  # Приведение к нижнему регистру для унификации проверки

    while status not in ['новая', 'в процессе', 'выполнена']:
        print("Неверный статус! Попробуйте снова.")
        status = input(f"Введите статус заметки (новая, в процессе, выполнена): ").lower()

    current_date = datetime.now().strftime("%d-%m-%Y")

    issue_date = input(
        f"Введите дату дедлайна (день-месяц-год), или оставьте пустым для использования даты по умолчанию ({get_default_issue_date()}): ")

    if not issue_date.strip():  # Если пользователь оставил поле пустым, используем значение по умолчанию
        issue_date = get_default_issue_date()
    else:
        while not validate_date(issue_date):
            print("Неверный формат даты! Введите дату в формате день-месяц-год.")
            issue_date = input(f"Введите дату дедлайна (день-месяц-год): ")

    note = {
        'username': username,
        'title': title,
        'content': content,
        'status': status.capitalize(),
        'created_date': current_date,
        'issue_date': issue_date
    }

    return note


# Вызываем функцию для демонстрации работы
if __name__ == "__main__":
    new_note = create_note()
    print("\nЗаметка создана:", new_note)