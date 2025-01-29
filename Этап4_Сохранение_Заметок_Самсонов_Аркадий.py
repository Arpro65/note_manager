import ruamel.yaml
from datetime import datetime

notes = [
    {
        "username": "Иван",
        "title": "Первая заметка",
        "content": "Это моя первая заметка.",
        "status": "Активная",
        "created_date": datetime.now(),
        "issue_date": datetime(2024, 12, 31)
    },
    {
        "username": "Анна",
        "title": "Вторая заметка",
        "content": "Эта заметка о чем-то важном.",
        "status": "Завершено",
        "created_date": datetime(2023, 10, 15),
        "issue_date": datetime(2023, 11, 30)
    }
]


def save_notes_to_file(notes, filename):
    try:
        # Создаем объект YAML
        yaml = ruamel.yaml.YAML()

        # Устанавливаем стиль представления для строковых значений
        yaml.default_flow_style = False

        # Открываем файл в режиме записи
        with open(filename, 'w', encoding='utf-8') as file:
            # Проходимся по каждому элементу списка заметок
            for i, note in enumerate(notes, start=1):
                # Формируем словарь для одной заметки
                note_dict = {
                    f"Заметка №{i}": {
                        "Имя пользователя": note["username"],
                        "Заголовок": note["title"],
                        "Описание": note["content"],
                        "Статус": note["status"],
                        "Дата создания": note["created_date"].strftime("%Y-%m-%d"),
                        "Дедлайн": note["issue_date"].strftime("%Y-%m-%d")
                    }
                }

                # Сохраняем текущую заметку в файл
                yaml.dump(note_dict, file)

                # Добавляем разделитель между заметками
                file.write("\n---\n")
    except OSError as e:
        print(f"Произошла ошибка при работе с файлом: {e}")
    except KeyError as e:
        print(f"В одном из элементов отсутствует необходимое поле: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# Вызов функции для сохранения заметок в файл
save_notes_to_file(notes, "notes.yaml")