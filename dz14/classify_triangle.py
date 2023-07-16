def classify_triangle(a, b, c):
    """
    Функция для классификации треугольника на основе длин его сторон.

    Args:
        a (float): Длина стороны a.
        b (float): Длина стороны b.
        c (float): Длина стороны c.

    Returns:
        str: Классификация треугольника:
            - "Треугольник разносторонний" для треугольника со всеми разными сторонами.
            - "Треугольник равносторонний" для треугольника со всеми равными сторонами.
            - "Треугольник равнобедренный" для треугольника с двумя равными сторонами.
            - "Треугольник не существует" если треугольник не может существовать с заданными сторонами.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не существует"
    elif a != b and a != c and b != c:
        return "Треугольник разносторонний"
    elif a == b == c:
        return "Треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"