#Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
#определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
#1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from itertools import combinations

def is_valid(arrangement):
    for queen1, queen2 in combinations(arrangement, 2):
        # Проверяем, находятся ли ферзи на одной вертикали или горизонтали
        if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
            return False

        # Проверяем, находятся ли ферзи на одной диагонали
        if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
            return False

    return True

# Пример входных данных - координаты 8 ферзей
# Формат: (x, y), где x - номер строки, y - номер столбца
queens = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 1), (6, 3), (7, 5), (8, 7)]

# Проверяем валидность расстановки ферзей
valid = is_valid(queens)

if valid:
    print("Ферзи не бьют друг друга")   
else:
    print("Ферзи бьют друг друга")


#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
#Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from itertools import combinations

def generate_arrangement():
    # Генерируем случайную расстановку ферзей
    queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return queens

def is_valid(arrangement):
    for queen1, queen2 in combinations(arrangement, 2):
        # Проверяем, находятся ли ферзи на одной вертикали или горизонтали
        if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
            return False

        # Проверяем, находятся ли ферзи на одной диагонали
        if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
            return False

    return True

successful_arrangements = []
while len(successful_arrangements) < 4:
    queens = generate_arrangement()
    if is_valid(queens):
        successful_arrangements.append(queens)

# Выводим успешные расстановки ферзей
for idx, arrangement in enumerate(successful_arrangements):
    print(f"Успешная расстановка {idx+1}: {arrangement}")
