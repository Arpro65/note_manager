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

    # Открываем файл в режиме записи, если файл не существует, он будет создан
    with open(filename, 'w', encoding='utf-8') as file:

        for i, note in enumerate(notes, start=1):

            file.write(f"Заметка № {i}" + "\n")
            file.write(f"Имя пользователя: {note['username']}\n")
            file.write(f"Заголовок: {note['title']}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date'].strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Дедлайн: {note['issue_date'].strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("---" + "\n\n")

# Вызов функции для сохранения заметок в файл
save_notes_to_file(notes, "notes.txt")