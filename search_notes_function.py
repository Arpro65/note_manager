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


def search_notes(notes, keywords=[], status=None):
    """
    Функция для поиска заметок по списку ключевых слов и/или статусу.

    :param notes: список заметок
    :param keywords: список ключевых слов для поиска (необязательно)
    :param status: статус для фильтрации (необязательно)
    :return: список заметок, удовлетворяющих условиям поиска
    """
    # Проверяем наличие заметок
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