import logging
import argparse

# Настройки логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("Треугольник не существует")

    def check_negative_sides(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise ValueError("Значение стороны не может быть отрицательным")

    def classify_triangle(self):
        if self.a != self.b and self.a != self.c and self.b !=  self.c:
            return "Треугольник разносторонний"
        elif self.a == self.b == self.c:
            return "Треугольник равносторонний"
        else:
            return "Треугольник равнобедренный"

def main():
    parser = argparse.ArgumentParser(description="Программа для классификации треугольников")
    parser.add_argument("a", type=int, help="Длина стороны a")
    parser.add_argument("b", type=int, help="Длина стороны b")
    parser.add_argument("c", type=int, help="Длина стороны c")
    args = parser.parse_args()

    try:
        triangle = Triangle(args.a, args.b, args.c)
        triangle.check_negative_sides()
        triangle.check_triangle()
        triangle_type = triangle.classify_triangle()
        print(triangle_type)

    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()


#Запуск программы из командной строки:
#main.py  три аргумента a, b и c, представляющих длины сторон треугольника