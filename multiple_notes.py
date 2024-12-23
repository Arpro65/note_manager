from datetime import datetime


def is_valid_date(date_string):
    """Проверка на валидность формата даты"""
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def create_note():
    """Создание заметки и возврат словаря с заметкой"""

    name = input("Введите имя пользователя: ").strip()
    title = input("Введите заголовок заметки: ").strip()

    # Проверка пустого заголовка
    if not title:
        print("Заголовок не может быть пустым!")
        return None

    description = input("Введите описание заметки: ").strip()

    # Проверка пустого описания
    if not description:
        print("Описание не может быть пустым!")
        return None

    status = input("Введите статус заметки (например, 'новая', 'в работе', 'завершена'): ").strip()
    creation_date = input("Введите дату создания (дд-мм-гггг): ").strip()

    # Проверка на корректность даты
    while not is_valid_date(creation_date):
        print("Некорректный формат даты. Пожалуйста, введите дату в формате дд-мм-гггг.")
        creation_date = input("Введите дату создания (дд-мм-гггг): ").strip()

    deadline = input("Введите дедлайн (дд-мм-гггг): ").strip()

    # Проверка на корректность дедлайна
    while not is_valid_date(deadline):
        print("Некорректный формат даты. Пожалуйста, введите дедлайн в формате дд-мм-гггг.")
        deadline = input("Введите дедлайн (дд-мм-гггг): ").strip()

    note = {
        'name': name,
        'title': title,
        'description': description,
        'status': status,
        'creation_date': creation_date,
        'deadline': deadline
    }

    return note


def display_notes(notes):
    """Отображение всех заметок"""
    if not notes:
        print("Нет созданных заметок.")
        return

    print("\nСписок заметок:")
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. Имя: {note['name']}")
        print(f"   Заголовок: {note['title']}")
        print(f"   Описание: {note['description']}")
        print(f"   Статус: {note['status']}")
        print(f"   Дата создания: {note['creation_date']}")
        print(f"   Дедлайн: {note['deadline']}\n")


def main():
    notes = []
    print("Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.")
    
    while True:

        user_input = input("Введите 'добавить' для создания заметки, 'стоп' для завершения работы: ").strip().lower()

        if user_input == 'стоп':
            break
        elif user_input == 'добавить':
            note = create_note()
            if note:
                notes.append(note)
                print("Заметка добавлена.")
        else:
            print("Некорректная команда, попробуйте снова.")

    display_notes(notes)


if __name__ == "__main__":
    main()

