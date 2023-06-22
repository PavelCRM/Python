import json
import csv
import pickle

class FileManager:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def read_csv(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    @staticmethod
    def write_csv(file_path, data):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def read_pickle(file_path):
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data

    @staticmethod
    def write_pickle(file_path, data):
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)

# Пример использования

# Чтение и запись JSON
data = {'name': 'John', 'age': 30, 'city': 'New York'}
FileManager.write_json('data.json', data)
loaded_data = FileManager.read_json('data.json')
print(loaded_data)  # {'name': 'John', 'age': 30, 'city': 'New York'}

# Чтение и запись CSV
data = [['Name', 'Age'], ['John', 30], ['Alice', 25], ['Bob', 35]]
FileManager.write_csv('data.csv', data)
loaded_data = FileManager.read_csv('data.csv')
print(loaded_data)  # [['Name', 'Age'], ['John', '30'], ['Alice', '25'], ['Bob', '35']]

# Чтение и запись Pickle
data = {'name': 'John', 'age': 30, 'city': 'New York'}
FileManager.write_pickle('data.pkl', data)
loaded_data = FileManager.read_pickle('data.pkl')
print(loaded_data)  # {'name': 'John', 'age': 30, 'city': 'New York'}
