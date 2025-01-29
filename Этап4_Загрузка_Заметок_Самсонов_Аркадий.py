import sys
import ruamel.yaml
import os


def load_notes_from_file(filename):
    """
    Загружает заметки из указанного YAML-файла и выводит их в консоль в оригинальном формате.

    :param filename: Путь к файлу с заметками.
    :raises FileNotFoundError: Если файл не найден.
    :raises PermissionError: Если нет прав на чтение файла.
    :raises Exception: При возникновении любой другой ошибки.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f'Файл {filename} не найден.')

    if not os.access(filename, os.R_OK):
        raise PermissionError(f'Нет прав на чтение файла {filename}.')

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            yaml = ruamel.yaml.YAML()
            documents = list(yaml.load_all(file))
            for doc in documents:
                if isinstance(doc, dict):
                    yaml.dump(doc, sys.stdout)
                    print("---")  # Разделитель между документами
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')


# Пример использования
if __name__ == "__main__":
    load_notes_from_file('notes.yaml')
