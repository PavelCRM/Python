from file_generator import FileGenerator
from file_sorter import FileSorter
from file_operations import FileOperations

class FileManager:
    @staticmethod
    def run():
        while True:
            print("\nFile Management Menu")
            print("1. Generate files")
            print("2. Sort files")
            print("3. File operations")
            print("4. Exit")
            choice = int(input("Выберите действие: "))
            if choice == 1:
                FileGenerator.generate_files()
                print("Файл успешно сгенерирован.")
            elif choice == 2:
                FileSorter.sort_files()
                print("Файлы успешно отсортированы.")
            elif choice == 3:
                FileOperations.file_menu()
            elif choice == 4:
                break
            else:
                print("Некорректный выбор.")

if __name__ == "__main__":
    FileManager.run()
