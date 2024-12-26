from datetime import datetime, timedelta


def validate_date(date_str):
    """Проверяет корректность формата даты 'день-месяц-год'."""
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def create_note():
    """Запрашивает у пользователя информацию для создания заметки и возвращает её в виде словаря."""
    username = input("Введите ваше имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()
    content = input("Введите описание заметки: ").strip()

    # Проверка на пустые значения заголовка и описания
    if not title or not content:
        print("Заголовок и описание не могут быть пустыми.")
        return None

    # Выбор статуса заметки
    statuses = ["новая", "в процессе", "выполнена"]
    print("Выберите статус заметки из следующего списка:")
    for i, status in enumerate(statuses, start=1):
        print(f"{i}. {status}")

    while True:
        status_choice = input("Введите номер статуса заметки: ").strip()
        if status_choice.isdigit() and 1 <= int(status_choice) <= len(statuses):
            status = statuses[int(status_choice) - 1]
            break
        else:
            print("Некорректный выбор статуса. Пожалуйста, попробуйте снова.")

    created_date = datetime.now().strftime("%d-%m-%Y")

    # Запрашиваем дату дедлайна
    issue_date_input = input(
        "Введите дату дедлайна (день-месяц-год) или нажмите Enter для установки по умолчанию (неделя от сегодня): ").strip()

    if issue_date_input == "":
        issue_date = (datetime.now() + timedelta(weeks=1)).strftime("%d-%m-%Y")
        print(f"Дата дедлайна по умолчанию установлена на: {issue_date}")
    else:
        while not validate_date(issue_date_input):
            print("Некорректный формат даты. Пожалуйста, введите в формате 'день-месяц-год'.")
            issue_date_input = input("Введите дату дедлайна: ").strip()
        issue_date = issue_date_input

    # Возвращаем данные заметки в виде словаря
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    return note


# Вызов функции и вывод результата
if __name__ == "__main__":
    note_data = create_note()
    if note_data:
        print("Созданная заметка: ")
        print(note_data)



