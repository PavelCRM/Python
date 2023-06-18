import os
from file_renamer import batch_rename_files
import random

def generate_files(directory, num_files):
    for i in range(num_files):
        file_path = os.path.join(directory, f"file{i + 1}.txt")
        with open(file_path, 'w') as file:
            file.write(f"This is file {i + 1}")

def main():
    # Получаем текущую директорию программы
    directory = os.path.dirname(os.path.abspath(__file__))

    # Генерируем файлы в текущей директории
    num_files = 7
    generate_files(directory, num_files)

    desired_name = "new"  # Желаемое конечное имя файлов
    min_digits = 3  # Минимальное количество цифр в порядковом номере
    max_digits = 6  # Максимальное количество цифр в порядковом номере
    source_extension = "txt"  # Расширение исходного файла
    target_extension = "txt"  # Желаемое расширение конечного файла
    name_range = [3, 6]  # Диапазон символов для использования в исходном имени (3-6 символы)

    batch_rename_files(directory, desired_name, min_digits, max_digits, source_extension, target_extension, name_range)

if __name__ == '__main__':
    main()

