import yaml
from pprint import pprint

def load_notes_from_file(filename):
    """Функция для загрузки заметок из файла и преобразования их в список словарей."""

    notes = []  # Создаем пустой список для хранения заметок

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Открываем файл в режиме чтения с поддержкой кодировки UTF-8
            content = file.read()  # Считываем весь контент файла
            lines = content.split('---')  # Разделяем содержимое файла на отдельные заметки по разделителю ---

            for note in lines:
                if note.strip():  # Проверяем, чтобы строка не была пустой
                    data = yaml.safe_load(note)  # Преобразуем строку в словарь с помощью YAML
                    notes.append(data)  # Добавляем словарь в список заметок

    except FileNotFoundError:
        print(f'Файл {filename} не найден.')  # Обработчик ошибки, если файл не существует

    return notes  # Возвращаем список заметок

# Пример использования
if __name__ == "__main__":
    notes = load_notes_from_file('notes.yaml')
    pprint(notes)
