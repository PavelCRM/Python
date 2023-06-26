import csv
import json
import math
import random


def quadratic_roots(a, b, c):
    """Нахождение корней квадратного уравнения"""
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return None


def generate_csv_file(filename, rows):
    """Генерация CSV файла с тремя случайными числами в каждой строке"""
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for _ in range(rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            writer.writerow(row)


def quadratic_roots_decorator(func):
    """Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из CSV файла"""

    def wrapper(filename):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(f"Roots of {a}x^2 + {b}x + {c}: {result}")

    return wrapper


def save_to_json_decorator(func):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в JSON файл"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            'function': func.__name__,
            'parameters': {
                'args': args,
                'kwargs': kwargs
            },
            'result': result
        }
        with open('function_results.json', 'a') as json_file:
            json.dump(data, json_file)
            json_file.write('\n')
        return result

    return wrapper


# Использование декораторов 

@quadratic_roots_decorator
def find_roots(a, b, c):
    return quadratic_roots(a, b, c)


@save_to_json_decorator
def my_function(arg1, arg2):
    return arg1 + arg2


# Генерация CSV файла
generate_csv_file('numbers.csv', 100)

# Вызов функции с декораторами
find_roots('numbers.csv')
my_function(10, 20)
