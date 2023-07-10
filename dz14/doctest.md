def classify_triangle(a, b, c):
    """
    Функция для классификации треугольника на основе длин его сторон.

    >>> classify_triangle(3, 4, 5)
    'Треугольник разносторонний'
    >>> classify_triangle(5, 5, 5)
    'Треугольник равносторонний'
    >>> classify_triangle(5, 5, 6)
    'Треугольник равнобедренный'
    >>> classify_triangle(1, 2, 4)
    'Треугольник не существует'
    """

    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"
    elif a != b and a != c and b != c:
        return "Треугольник разносторонний"
    elif a == b == c:
        return "Треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"
