
from datetime import datetime

def проверить_дедлайн():
    while True:
        # Запрос у пользователя даты дедлайна
        issue_date_input = input("Введите дату дедлайна (в формате ДД.ММ.ГГГГ): ")

        try:
            # Преобразование введенной строки в объект datetime
            issue_date = datetime.strptime(issue_date_input, "%d.%m.%Y")
            break  # Если преобразование прошло успешно, выходим из цикла

        except ValueError:
            # Обработка ошибки при неверном формате даты
            print("Некорректный формат даты. Пожалуйста, попробуйте снова.")

    # Получение текущей даты
    current_date = datetime.now()

    # Определение, истек ли дедлайн
    if issue_date < current_date:
        # Рассчитываем разницу в днях
        days_overdue = (current_date - issue_date).days
        print(f"Дедлайн истек на {days_overdue} {'день' if days_overdue == 1 else 'дня'} назад.")
    else:
        # Рассчитываем количество оставшихся дней
        days_remaining = (issue_date - current_date).days
        print(f"Дедлайн еще не истек. Осталось {days_remaining} {'день' if days_remaining == 1 else 'дня'}.")

# Запуск функции для проверки дедлайна
проверить_дедлайн()

