import re  # Импортируем модуль регулярных выражений для поиска чисел в строке
from datetime import datetime


def get_max_note_number(filename):
    """
    Функция ищет максимальную нумерацию заметок в файле.

    :param filename: Имя файла, в котором ищется максимальная нумерация заметок.
    :return: Максимальный номер заметки или 0, если файл пустой или не найден.
    """
    max_number = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()  # Читаем строку из файла
                if not line:  # Если строка пустая, значит достигли конца файла
                    break
                if line.startswith("Заметка №"):  # Проверяем, начинается ли строка с "Заметка №"
                    match = re.search(r'\d+', line)  # Находим первое число в строке
                    if match:
                        number = int(match.group())  # Извлекаем номер заметки
                        if number > max_number:  # Обновляем максимум, если нашли больший номер
                            max_number = number
    except FileNotFoundError:  # Если файл не найден, просто возвращаем 0
        pass
    except PermissionError as e:
        print(f"У вас недостаточно прав для записи в файл: {e}")
    except OSError as e:
        print(f"Произошла ошибка при записи в файл: {e}")

    return max_number


def append_notes_to_file(notes, filename='notes.yaml'):
    """
    Функция добавляет новые заметки в указанный файл, сохраняя уникальность номеров.

    :param notes: Список заметок, которые должны быть добавлены в файл.
    :param filename: Имя файла, куда будут добавлены заметки (по умолчанию 'notes.yaml').
    """
    current_note_number = get_max_note_number(filename) + 1  # Определяем следующий свободный номер заметки

    with open(filename, 'a', encoding='utf-8') as file:
        for note in notes:
            # Формируем структуру данных для записи в YAML
            file.write(f'Заметка №{current_note_number}:\n')  # Записываем номер заметки
            file.write(f'  Имя пользователя: {note.get("username", "")}\n')  # Записываем имя пользователя
            file.write(f'  Заголовок: {note.get("title", "")}\n')  # Записываем заголовок
            file.write(f'  Описание: {note.get("content", "")}\n')  # Записываем описание
            file.write(f'  Статус: {note.get("status", "")}\n')  # Записываем статус
            file.write(f'  Дата создания: {note.get("created_date", datetime.now().strftime("%Y-%m-%d"))}\n')  # Записываем дату создания
            file.write(f'  Дедлайн: {note.get("issue_date", "")}\n')  # Записываем дедлайн
            file.write("\n---\n")  # Разделяем заметки тройным дефисом

            current_note_number += 1  # Увеличиваем счетчик для следующей заметки


# Пример использования функции
if __name__ == "__main__":
    notes = [
        {
            'username': 'Иван Иванов',
            'title': 'Заметка 1',
            'content': 'Это первая добавленная заметка.',
            'status': 'Новая',
            'created_date': '2023-10-01',
            'issue_date': '2023-11-30'
        },
        {
            'username': 'Пётр Петров',
            'title': 'Заметка 2',
            'content': 'Это вторая добавленная заметка.',
            'status': 'В процессе',
            'created_date': '2023-09-15',
            'issue_date': '2023-10-31'
        }
    ]

    append_notes_to_file(notes)  # Вызываем функцию для добавления заметок в файл