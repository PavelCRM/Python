# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.


class TriangleError(Exception):
    pass

class InvalidTriangleError(TriangleError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NonexistentTriangleError(TriangleError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NegativeSideError(TriangleError):
    def __init__(self, side):
        self.side = side
        message = f"Значение стороны  {side} не может быть отрицательным"
        super().__init__(message)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise NonexistentTriangleError("Треугольник не существует")

    def check_negative_sides(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            if self.a < 0:
                raise NegativeSideError('a')
            if self.b < 0:
                raise NegativeSideError('b')
            if self.c < 0:
                raise NegativeSideError('c')

    def classify_triangle(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return "Треугольник разносторонний"
        elif self.a == self.b == self.c:
            return "Треугольник равносторонний"
        else:
            return "Треугольник равнобедренный"


try:
    a = int(input("Введите сторону треугольника a: "))
    b = int(input("Введите сторону треугольника b: "))
    c = int(input("Введите сторону треугольника c: "))

    triangle = Triangle(a, b, c)
    triangle.check_negative_sides()
    triangle.check_triangle()
    triangle_type = triangle.classify_triangle()
    print(triangle_type)

except ValueError:
    print("Ошибка: Введите числовые значения для сторон треугольника")

except NegativeSideError as e:
    print(f"Ошибка: {e.side} значение не может быть отрицательным")

except NonexistentTriangleError as e:
    print("Ошибка: " + e.message)

except TriangleError as e:
    print("Ошибка: " + str(e))
