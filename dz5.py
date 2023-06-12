#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла

import os

def parse_file_path(file_path):
    path, file = os.path.split(file_path)
    name, extension = os.path.splitext(file)
    return (path, name, extension)

path, name, extension = parse_file_path('/Users/UserName/Desktop/example.py')
print(f'Path: {path}')
print(f'Name: {name}')
print(f'Extension: {extension}')

#Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
#длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
#В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#Сумма рассчитывается как ставка умноженная на процент премии


names = ['Алиса', 'Тимур', 'Евгений']
rates = []

for name in names:
    rate = int(input(f'Введите ставку для {name}: '))
    rates.append(rate)

bonuses = ['10%', '15%', '25%']

result = {name: rate * float(bonus[:-1])/100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result)


#Создайте функцию генератор чисел Фибоначчи 

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()
for i in range(15):
    print(next(fib))  # вывод первых 15 чисел Фибоначчи