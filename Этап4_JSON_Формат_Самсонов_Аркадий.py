import json

# Функция для сохранения заметок в формате JSON
def save_notes_json(notes, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

# Список заметок
notes = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    },
    {
        "username": "Иван",
        "title": "Отчет",
        "content": "Написать отчет о проделанной работе",
        "status": "в процессе",
        "created_date": "28-11-2024",
        "issue_date": "01-12-2024"
    }
]

# Сохранение заметок в файл notes.json
save_notes_json(notes, 'notes.json')
print("Заметки успешно сохранены в файл notes.json")
