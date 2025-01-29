def load_notes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        # Если файл отсутствует, создаём его и выводим сообщение
        print(f'Файл {filename} не найден. Создан новый файл.')
        open(filename, 'w').close()  # Создаём пустой файл
        return None
    except PermissionError:
        # Если отсутствуют права доступа к файлу
        print(f'Отсутствуют права доступа к файлу {filename}. Обратитесь к администратору.')
        return None
    except OSError as e:
        # Если файл повреждён или возникли другие системные ошибки
        print(f'Ошибка при чтении файла {filename}. Проверьте его содержимое.')
        print(f'Подробная информация об ошибке: {e}')
        return None
    except Exception as e:
        # Обработка других возможных исключений
        print(f'Произошла непредвиденная ошибка при работе с файлом {filename}:')
        print(f'Подробная информация об ошибке: {e}')
        return None

# Пример использования функции
file_path = 'example.txt'
data = load_notes_from_file(file_path)
if data is not None:
    print('Данные успешно прочитаны:')
    print(data)
else:
    print('Не удалось прочитать данные из файла.')