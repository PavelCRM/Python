import os
import shutil

class FileSorter:
    @staticmethod
    def sort_files():
        file_extensions = {
            "txt": "txt_files",
            "docx": "docx_files",
            "doc": "doc_files"
        }
        for file_name in os.listdir():
            if os.path.isfile(file_name):
                file_extension = file_name.split(".")[-1]
                if file_extension in file_extensions:
                    directory = file_extensions[file_extension]
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    shutil.move(file_name, os.path.join(directory, file_name))
