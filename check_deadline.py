from datetime import datetime

def get_deadline():
    while True:
        date_input = input("Введите дату дедлайна (дд-мм-гггг): ")
        try:
            # Преобразуем строку в объект datetime
            deadline = datetime.strptime(date_input, "%d-%m-%Y")
            return deadline
        except ValueError:
            print("Неверный формат даты! Пожалуйста, используйте формат дд-мм-гггг.")

def check_deadline(deadline):
    current_date = datetime.now()
    if deadline < current_date:
        print("Внимание! Дедлайн истёк!")
    else:
        remaining_days = (deadline - current_date).days
        print(f"Дедлайн не истёк. Осталось дней: {remaining_days}")

def main():
    deadline = get_deadline()
    check_deadline(deadline)

if __name__ == "__main__":
    main()