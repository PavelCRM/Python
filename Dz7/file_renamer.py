import os
import random

def batch_rename_files(directory, desired_name, min_digits, max_digits, source_extension, target_extension, name_range=None):
    # Получаем путь к каталогу с файлами из текущего модуля
    current_directory = os.path.dirname(os.path.abspath(__file__))
    target_directory = os.path.join(current_directory, directory)

    # Получаем список файлов в указанном каталоге
    files = os.listdir(target_directory)

    # Фильтруем файлы по расширению
    source_files = [file for file in files if file.endswith(source_extension)]

    # Проверяем наличие файлов для переименования
    if not source_files:
        print("Нет файлов с указанным расширением в заданном каталоге.")
        return

    # Определяем диапазон символов для использования в исходном имени
    if name_range is not None:
        start = name_range[0] - 1  # Корректируем индексацию
        end = name_range[1]
    else:
        start = 0
        end = None

    # Получаем базовое имя для переименования
    base_name = desired_name[start:end] if desired_name else ""

    # Перебираем файлы и выполняем переименование
    for i, file in enumerate(source_files):
        # Генерируем случайное количество цифр в порядковом номере файла
        num_digits = random.randint(min_digits, max_digits)
        count = str(i).zfill(num_digits)

        # Формируем новое имя файла
        new_name = f"{base_name}{count}.{target_extension}"

        # Получаем полный путь к файлу
        file_path = os.path.join(target_directory, file)

        # Получаем полный путь к новому файлу
        new_file_path = os.path.join(target_directory, new_name)

        # Запрашиваем подтверждение на переименование файла
        confirmation = input(f"Переименовать файл {file} в {new_name}? (Y/N): ")
        if confirmation.lower() == 'y':
            # Переименовываем файл
            os.rename(file_path, new_file_path)
            # Выводим информацию о переименовании
            print(f"Переименован файл: {file} -> {new_name}")
        else:
            print(f"Пропущено переименование файла: {file}")

