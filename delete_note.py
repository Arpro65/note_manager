# Список для хранения заметок
notes = [
    {"username": "Алексей", "title": "Первая заметка", "content": "Это первая заметка."},
    {"username": "Мария", "title": "Вторая заметка", "content": "Это вторая заметка."},
    {"username": "Алексей", "title": "Список покупок", "content": "Молоко, хлеб."}
]

def delete_notes():
    # Запрашиваем у пользователя имя пользователя или заголовок заметки
    search_term = input("Введите имя пользователя или заголовок заметки для удаления: ").strip()
    if not notes:
        print("Список заметок пуст.")
        return

    # Флаг для отслеживания, были ли найдены заметки
    found = False

    # Проходим по списку заметок
    for note in notes[:]:  # Используем срез, чтобы менять список в процессе итерации
        if search_term.lower() in note["username"].lower() or search_term.lower() in note["title"].lower():
            # Подтверждение удаления
            confirm = input(f"Вы уверены, что хотите удалить заметку '{note['title']}' (да/нет)? ").strip().lower()
            if confirm == 'да':
                notes.remove(note)
                print(f"Заметка '{note['title']}' успешно удалена.")
                found = True

    if not found:
        print("Заметка не найдена.")

    # Вывод обновлённого списка заметок
    print("Обновленный список заметок:")
    for note in notes:
        print(f"{note['username']} - {note['title']}: {note['content']}")

# Запуск функции удаления заметок
delete_notes()