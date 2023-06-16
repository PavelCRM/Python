from file_renamer import batch_rename_files

directory = 'e:/учеба/Python/Dz7/proverka'  # Укажите путь к каталогу с файлами
desired_name = "new"  # Желаемое конечное имя файлов
num_digits = 3  # Количество цифр в порядковом номере
source_extension = "txt"
target_extension = "py"  # Желаемое расширение целевых файлов

batch_rename_files(directory, desired_name, num_digits, source_extension, target_extension)
