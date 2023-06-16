import os

def batch_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    # Получаем список файлов в указанном каталоге
    files = os.listdir(directory)

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
        # Генерируем порядковый номер с указанным количеством цифр
        count = str(i).zfill(num_digits)

        # Формируем новое имя файла
        new_name = f"{base_name}{count}.{target_extension}"

        # Получаем полный путь к файлу
        file_path = os.path.join(directory, file)

        # Получаем полный путь к новому файлу
        new_file_path = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(file_path, new_file_path)

        # Выводим информацию о переименовании
        print(f"Переименован файл: {file} -> {new_name}")
