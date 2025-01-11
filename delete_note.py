# Функция для вывода текущих заметок
def print_notes(notes):
    if not notes:
        print("Нет заметок.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['имя']}")
        print(f"   Заголовок: {note['заголовок']}")
        print(f"   Описание: {note['описание']}\n")


# Функция для удаления заметок по заданному критерию
def delete_note(notes, criterion, value):
    deleted_count = 0
    original_length = len(notes)

    # Перебираем заметки и удаляем те, которые соответствуют критерию
    notes[:] = [note for note in notes if note[criterion].lower() != value.lower()]

    # Выводим результат
    if len(notes) == original_length:
        print(f'Заметок с "{value}" не найдено.')
    else:
        deleted_count = original_length - len(notes)
        print(f"Удалено {deleted_count} заметок.")

    return notes


# Основная функция программы
def main():
    # Пример списка заметок
    notes = [
        {
            'имя': 'Алексей',
            'заголовок': 'Список покупок',
            'описание': 'Купить продукты на неделю'
        },
        {
            'имя': 'Мария',
            'заголовок': 'Учеба',
            'описание': 'Подготовиться к экзамену'
        }
    ]

    while True:
        print("\nВот текущий список ваших заметок:")
        print_notes(notes)

        # Запрашиваем у пользователя критерий для удаления
        choice = input("Что вы хотите сделать?\n"
                       "1. Удалить заметку по имени пользователя\n"
                       "2. Удалить заметку по заголовку\n"
                       "3. Завершить работу\n"
                       "Ваш выбор: ")

        if choice == '3':
            break

        elif choice == '1':
            user_name = input("Введите имя пользователя для удаления заметки: ").strip()
            notes = delete_note(notes, 'имя', user_name)

        elif choice == '2':
            title = input("Введите заголовок для удаления заметки: ").strip()
            notes = delete_note(notes, 'заголовок', title)

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()