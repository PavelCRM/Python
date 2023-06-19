class FileGenerator:
    @staticmethod
    def generate_files():
        file_name = input("Введите имя генерируемого файла: ")
        file_extension = input("Введите расширение файла: ")
        file_name_with_extension = f"{file_name}.{file_extension}"

        with open(file_name_with_extension, "w") as file:
            file.write("Пример содержимого файла.")
