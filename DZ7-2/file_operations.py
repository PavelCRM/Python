import os

class FileOperations:
    @staticmethod
    def file_menu():
        file_name = input("Введите имя файла: ")
        if os.path.isfile(file_name):
            print("1. Просмотр файла")
            print("2. Запись в файл")
            print("3. Переименование файла")
            print("4. Удаление файла")
            choice = int(input("Выберите действие: "))
            if choice == 1:
                FileOperations.view_file(file_name)
            elif choice == 2:
                FileOperations.write_file(file_name)
            elif choice == 3:
                FileOperations.rename_file(file_name)
            elif choice == 4:
                FileOperations.delete_file(file_name)
            else:
                print("Некорректный выбор.")
        else:
            print("Файл не существует.")

    @staticmethod
    def view_file(file_name):
        with open(file_name, "r") as file:
            content = file.read()
            print("Содержимое файла:\n", content)

    @staticmethod
    def write_file(file_name):
        with open(file_name, "a") as file:
            content = input("Введите текст для записи в файл: ")
            file.write(content)
            print("Текст успешно записан в файл.")

    @staticmethod
    def rename_file(file_name):
        new_file_name = input("Введите новое имя файла: ")
        try:
            os.rename(file_name, new_file_name)
            print("Файл успешно переименован.")
        except Exception as e:
            print("Ошибка при переименовании файла:", str(e))

    @staticmethod
    def delete_file(file_name):
        os.remove(file_name)
        print("Файл успешно удален.")
