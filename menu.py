import sys
from colorama import Fore, Style, init

# Инициализация Colorama для вывода цветного текста
init(autoreset=True)


def create_note():
    print(Fore.GREEN + "Новая заметка создана!" + Style.RESET_ALL)


def display_notes():
    print(Fore.BLUE + "Все заметки показаны." + Style.RESET_ALL)


def update_note():
    print(Fore.YELLOW + "Заметка обновлена." + Style.RESET_ALL)


def delete_note():
    confirmation = input("Вы уверены, что хотите удалить заметку? (Y/N): ")
    if confirmation.lower() == 'y':
        print(Fore.RED + "Заметка удалена." + Style.RESET_ALL)
    else:
        print("Удаление отменено.")


def search_notes():
    print(Fore.CYAN + "Поиск выполнен. Результаты показаны." + Style.RESET_ALL)


def exit_program():
    print(Fore.MAGENTA + "Программа завершена. Спасибо за использование!" + Style.RESET_ALL)
    sys.exit(0)


def main_menu():
    print("\nМеню действий:")
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Найти заметки")
    print("6. Выйти из программы\n")

    choice = input("Ваш выбор: ")

    # Проверяем ввод пользователя
    try:
        choice = int(choice)

        if choice == 1:
            create_note()
        elif choice == 2:
            display_notes()
        elif choice == 3:
            update_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            search_notes()
        elif choice == 6:
            exit_program()
        else:
            print(Fore.RED + "Неверный выбор. Пожалуйста, выберите действие из списка." + Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + "Ошибка! Вы ввели не число. Попробуйте снова." + Style.RESET_ALL)


if __name__ == "__main__":
    while True:
        main_menu()